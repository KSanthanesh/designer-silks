/*
    Core logic/payment flow for this comes from here:
    https://stripe.com/docs/payments/accept-a-payment
    CSS from here: 
    https://stripe.com/docs/stripe-js
*/
let stripePublicKey = $('#id_stripe_public_key').text().slice(1, -1);
let clientSecret = $('#id_client_secret').text().slice(1, -1);
let stripe = Stripe(stripePublicKey);
let elements = stripe.elements();

let style = {
    base: {
        color: '#000',
        fontSize: '16px',
        fontFamily: 'poppins',
        '::placeholder': {
            color: '#aab7c4'
        }
    },
    invalid: {
        color: '#dc3545',
        iconColor: '#dc3545'
    }
}
let card = elements.create('card', {style: style});
card.mount('#card-element');

// To handle realtime validation errors on the card element

card.addEventListener('change', function(event) {
    let errorElement = document.getElementById('card-errors');
    if(event.error) {
        let html = `
        <span class="fa-icon" role="alert">
        <i class="fas fa-times"></i></span>
        <span>${event.error.message}</span>
        `;
        $(errorElement).html(html)
    } else {
        errorElement.textContent = '';
    }
})

// Create a token or display an error when the form is submitted.
var form = document.getElementById('payment-form');
form.addEventListener('submit', function(ev) {
    ev.preventDefault();
    card.update({ 'disabled': true})
    $('#submit-btn').attr('disabled', true)
    $('#payment-form').fadeToggle(100);
    $('#loading-screen').fadeToggle(100);

    let saveInfo = Boolean($('#id-save-info').attr('checked'));
    // Using the csrf_token from the form
    let csrfToken = $('input[name="csrfmiddlewaretoken"]').val();
    let postData = {
        'csrfmiddlewaretoken': csrfToken,
        'client_secret': clientSecret,
        'save_info': saveInfo,
    };
    let url = '/checkout/cache_checkout_data/';

    $.post(url, postData).done(function() {
        stripe.confirmCardPayment(clientSecret, {
            payment_method: {
                card: card,
                billing_details: {
                    name: $.trim(form.first_name.value) +''+ $.trim(form.last_name.value),
                    email: $.trim(form.email.value),
                    phone: $.trim(form.phone_number.value),
                    address: {
                        line1: $.trim(form.address_line1.value),
                        line2: $.trim(form.address_line2.value),
                        city: $.trim(form.county_or_city.value),
                        country: $.trim(form.country.value),
                    }
                }
            },
            shipping: {
                    name: $.trim(form.first_name.value) +''+ $.trim(form.last_name.value),
                    phone: $.trim(form.phone_number.value),
                    address: {
                        line1: $.trim(form.address_line1.value),
                        line2: $.trim(form.address_line2.value),
                        city: $.trim(form.county_or_city.value),
                        postal_code: $.trim(form.postcode.value),
                        country: $.trim(form.country.value),
                    }
                },
        }).then(function(result) {
            if (result.error) {
                var errorElement = document.getElementById('card-errors');
                var html = `
                    <span class="icon" role="alert">
                    <i class="fas fa-times"></i>
                    </span>
                    <span>${result.error.message}</span>`;
                $(errorElement).html(html);
                $('#payment-form').fadeToggle(100);
                $('#loading-screen').fadeToggle(100);
                card.update({ 'disabled': false});
                $('#submit-btn').attr('disabled', false);
            } else {
                if (result.paymentIntent.status === 'succeeded') {
                    form.submit();
                }
            }
        });
    }).fail(function() {
        // just reload the page, the error will be in django messages
        location.reload();
    }) 
});

