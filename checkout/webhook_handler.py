""" Webhook Handler"""

from django.http import HttpResponse


class StripeWH_Handler:
    """ To handle Stripe Webhooks """

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        To handle a generic /unknown / unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}', status=200
        )

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment intent succeeded from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment intent payment failed from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}', status=200
        )
