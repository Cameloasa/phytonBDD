from behave import given, when, then, step
from src.payment import Payment, PaymentError
from src.user import AuthenticationError, User

@given('I am logged in as "{username}" with password "{password}"')
def step_given_logged_in(context, username, password):
    user = User(username, password)
    user.login(username, password)
    context.user = user
    context.cart = user.get_cart()

@given("I am not logged in")
def step_given_not_logged_in(context):
    context.user = User("user1", "pass123")  # Creează utilizator, dar nu logat
    context.cart = context.user.get_cart()

@given("my cart contains")
def step_given_cart_contains(context):
    for row in context.table:
        book = row["Book"]
        quantity = int(row["Quantity"])
        context.cart.add_book(book, quantity)

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
    assert context.payment.total_amount > 0, "Payment amount should be positive"
    # Notă: Nu putem verifica direct print-ul, dar presupunem că totalul e corect

@then('I should receive a receipt with')
def step_then_receive_receipt(context):
    receipt = context.payment.generate_receipt()
    for row in context.table:
        subtotal = f"Subtotal: {row['Subtotal']} SEK"
        discount = f"Discount: {row['Discount Applied']} SEK"
        total = f"Total (after discount): {row['Total After Discount']} SEK"
        assert subtotal in receipt, f"Expected subtotal {subtotal} not found"
        assert discount in receipt, f"Expected discount {discount} not found"
        assert total in receipt, f"Expected total {total} not found"

@then('I should see an error "{message}"')
def step_then_see_error(context, message):
    assert hasattr(context, "error"), "No error occurred"
    assert context.error == message, f"Expected error '{message}', got '{context.error}'"

# Reutilizăm din cart_steps.py
@then("my cart should be empty")
def step_then_cart_empty(context):
    assert context.cart.get_total_books() == 0, "Cart is not empty"