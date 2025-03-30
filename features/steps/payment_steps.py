from behave import given, when, then
from src.payment import Payment, PaymentError
from src.user import AuthenticationError, User

@given("I am not logged_in")
def step_given_not_logged_in(context):
    context.user = User("user1", "pass123")
    context.cart = None

@given("my cart contains")
def step_given_cart_contains(context):
    for row in context.table:
        book = row["Book"]
        quantity = int(row["Quantity"])
        context.cart.add_book(book, quantity)

@given("my cart is empty")
def step_given_cart_empty(context):
    context.cart.empty_cart()

@when('I process payment with "card"')
def step_when_process_payment(context):
    try:
        payment = Payment(context.user)
        payment.process_payment("card")
        context.payment = payment
    except (AuthenticationError, PaymentError) as e:
        context.error = str(e)

@then('I should see a payment confirmation "{message}"')
def step_then_payment_confirmation(context, message):
    assert hasattr(context, "payment"), "Payment failed unexpectedly"
    assert context.payment.confirmation_message == message, f"Expected '{message}', got '{context.payment.confirmation_message}'"
    assert context.payment.total_amount == 45.00, f"Expected 45.00, got {context.payment.total_amount}"

@then('I should receive a receipt with')
def step_then_receive_receipt(context):
    receipt = context.payment.generate_receipt()
    for row in context.table:
        subtotal = f"Subtotal: {row['Subtotal']} SEK"
        discount = f"Discount: {row['Discount']} SEK"
        total = f"Total (after discount): {row['Total After Discount']} SEK"
        assert subtotal in receipt, f"Expected {subtotal} not found"
        assert discount in receipt, f"Expected {discount} not found"
        assert total in receipt, f"Expected {total} not found"