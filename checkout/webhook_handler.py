from django.http import HttpResponse
from .models import Order, OrderLineItem
from merch.models import Merch
from profiles.models import UserProfile

import json
import time


class StripeWebhookHandler:
    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200,
        )

    def handle_payment_intent_succeeded(self, event):
        intent = event.data.object
        payment_id = intent.id
        cart = intent.nmetadata.cart
        save_info = intent.metadata.save_info
        billing_details = intent.charges.data[0].billing_details
        delivery_details = intent.delivery
        grand_total = round(intent.charges.data[0].amount / 100, 2)

        for field, value in delivery_details.address.items():
            if value == '':
                delivery_details.address[field] = None

        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            profile = UserProfile.objects.get(user__username=username)
            if save_info:
                profile.default_phone_number = delivery_details.phone
                profile.default_country = delivery_details.address.country
                profile.default_postcode = delivery_details.address.postcode
                profile.default_town_or_city = delivery_details.address.town_or_city
                profile.default_street_address1 = delivery_details.address.street_address1
                profile.default_street_address2 = delivery_details.address.street_address2
                profile.default_county = delivery_details.address.county
                profile.save()

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order = Order.objects.get(
                    full_name__iexact=delivery_details.name,
                    email__iexact=billing_details.email,
                    phone_number__iexact=delivery_details.phone,
                    country__iexact=delivery_details.address.country,
                    postcode__iexact=delivery_details.address.postcode,
                    town_or_city__iexact=delivery_details.address.town_or_city,
                    street_address1__iexact=delivery_details.address.street_address1,
                    street_address2__iexact=delivery_details.address.street_address2,
                    county__iexact=delivery_details.address.county,
                    grand_total__iexact=delivery_details.grand_total,
                    original_cart=cart,
                    stripe_payment_id=payment_id,
                )
                order_exists = True
                break

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)
        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Order already exists in the database.',
                status=200,
            )
        else:
            order = None
            try:
                order = Order.objects.create(
                    full_name=delivery_details.name,
                    user_profile=profile,
                    email=billing_details.email,
                    phone_number=delivery_details.phone,
                    country=delivery_details.address.country,
                    postcode=delivery_details.address.postcode,
                    town_or_city=delivery_details.address.town_or_city,
                    street_address1=delivery_details.address.street_address1,
                    street_address2=delivery_details.address.street_address2,
                    county=delivery_details.address.county,
                    original_cart=cart,
                    stripe_payment_id=payment_id,
                )
                for item_id, item_data in json.loads(cart).items():
                    item = Merch.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        order_line_item = OrderLineItem(
                            order=order,
                            item=item,
                            quantity=item_data,
                        )
                        order_line_item.save()
                    else:
                        for size, quantity in item_data['items_by_size'].items():
                            order_line_item = OrderLineItem(
                                order=order,
                                item=item,
                                quantity=quantity,
                                item_size=size
                            )
                            order_line_item.save()
            except Exception as e:
                if order:
                    order.delete()
                return HttpResponse(
                    content=f'Webhook received: {event["type"]} | ERROR: {e}',
                    status=500,
                )

        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200,
        )

    def handle_payment_intent_payment_failed(self, event):
        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Order created in webhook.',
            status=200,
        )
