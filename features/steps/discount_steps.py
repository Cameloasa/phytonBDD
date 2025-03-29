from behave import given, when, then
from cart import Cart

@when(u'I apply the discount')
def step_when_apply_discount(context):
    context.total_with_discount = context.cart.apply_discount()
