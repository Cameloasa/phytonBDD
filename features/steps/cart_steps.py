from behave import given, when, then
from cart import Cart

@given("I have an empty cart")
def step_given_empty_cart(context):
    context.cart = Cart()

@given('I have a cart with {initial:d} copies of "{book}"')
def step_given_cart_with_books(context, initial, book):
    context.cart = Cart()
    context.cart.add_book(book, initial)

@when('I add {quantity:d} copies of "{book}" to the cart')
def step_when_add_book(context, quantity, book):
    context.cart.add_book(book, quantity)

@when('I remove {quantity:d} copies of "{book}" from the cart')
def step_when_remove_book(context, quantity, book):
    context.cart.remove_book(book, quantity)

@then("the cart should contain {expected:d} books")
def step_then_check_cart_count(context, expected):
    assert context.cart.get_total_books() == expected, f"Expected {expected} books, but found {context.cart.get_total_books()}"

@then("the total amount should be {expected:d}")
def step_then_check_total_amount(context, expected):
    assert context.cart.get_total_amount() == expected, f"Expected total amount {expected}, but found {context.cart.get_total_amount()}"

@then('"{book}" should appear as {quantity:d} copies on one line')
def step_then_check_book_quantity(context, book, quantity):
    assert book in context.cart.items, f"{book} not found in cart"
    assert context.cart.items[book]["quantity"] == quantity, f"Expected {quantity} copies of {book}, but found {context.cart.items[book]['quantity']}"