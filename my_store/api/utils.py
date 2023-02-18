import os

import stripe
from dotenv import load_dotenv

load_dotenv()


def get_price_id(item):
    """Получение price_id и product_id."""
    stripe.api_key = os.getenv('API_KEY')
    product_id = stripe.Product.create(name=item.name)
    price_id = stripe.Price.create(
        product=product_id,
        unit_amount=item.price,
        currency=item.currency
    )

    return price_id


def get_session_id(price_id, amount=1):
    session_id = stripe.checkout.Session.create(
        mode="payment",
        line_items=[{"price": price_id, "quantity": amount}],
        success_url=(
            "https://example.com/success?session_id={CHECKOUT_SESSION_ID}"),
        cancel_url="https://example.com/cancel",
    )

    return session_id
