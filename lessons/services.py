import stripe

from config.settings import STRIPE_API_KEY

stripe.api_key = STRIPE_API_KEY


def create_stripe_product(instance):

    title_product = f'{instance.paid_course}' if instance.paid_course else f'{instance.paid_lesson}'
    stripe_product = stripe.Product.create(name=f"{title_product}")
    return stripe_product.get('id')


def create_stripe_price(summ, stripe_product_id):
    return stripe.Price.create(
        currency="rub",
        unit_amount=summ * 100,
        product=stripe_product_id
    )


def create_stripe_session(summ):
    session = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": summ.get('id'), "quantity": 1}],
        mode="payment",
    )
    return session.get('id'), session.get('url')
