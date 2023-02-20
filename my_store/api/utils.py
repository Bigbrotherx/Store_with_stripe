import os

import stripe
from dotenv import load_dotenv


load_dotenv()
stripe.api_key = os.getenv('API_KEY')


def create_product_id(item):
    """Создание product_id если его нет."""
    if item.product_id:

        return

    product_id = stripe.Product.create(name=item.name)
    item.product_id = product_id.id
    item.save(update_fields=['product_id'])


def get_price_id(item):
    """Получение price_id"""
    price_id = stripe.Price.create(
        product=item.product_id,
        unit_amount=item.price,
        currency=item.currency
    )

    return price_id.id


def get_create_coupons_id(coupon):
    """Получение id созданого купона."""
    if not coupon.discount_id:
        discount_id = stripe.Coupon.create(
            id=coupon.discount_name,
            percent_off=coupon.percent_off,
            duration=coupon.duration,
        )
        coupon.discount_id = discount_id.id
        coupon.save(update_fields=['discount_id'])
    return coupon.discount_id


def create_session_id(price_amount_tuple, discount_id=None):
    """Созание сессии оплаты одного или нескольких товаров"""
    list_items = [
        {"price": price_id, "quantity": amount}
        for price_id, amount in price_amount_tuple]
    discounts = [{'coupon': discount_id}] if discount_id else []
    session_id = stripe.checkout.Session.create(
        mode="payment",
        line_items=list_items,
        discounts=discounts,
        success_url=(
            "https://example.com/success?session_id={CHECKOUT_SESSION_ID}"),
        cancel_url="https://example.com/cancel",
    )

    return session_id
