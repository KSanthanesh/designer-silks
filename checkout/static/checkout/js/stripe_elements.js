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
form.addEventListener('submit', function(event) {
  event.preventDefault();
  card.update({ 'disabled': true})
  $('#submit-btn').attr('disabled', true)

  stripe.confirmCardPayment(clientSecret, {
    payment_method: {
        card: card,
    }
}).then(function(result) {
    if (result.error) {
        var errorElement = document.getElementById('card-errors');
        var html = `
            <span class="icon" role="alert">
            <i class="fas fa-times"></i>
            </span>
            <span>${result.error.message}</span>`;
        $(errorElement).html(html);
        card.update({ 'disabled': false});
        $('#submit-btn').attr('disabled', false);
    } else {
        if (result.paymentIntent.status === 'succeeded') {
            form.submit();
        }
    }
});
});

