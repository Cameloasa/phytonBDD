from behave import given, when, then
from cart import Cart

@given("I have an empty cart")
def step_given_empty_cart(context):
    # This will create an empty cart later
    context.cart = Cart()

@when('I add 1 copy of "{book}" to the cart')
def step_when_add_book(context, book):
    # This will add the book to the cart later
    context.cart.add_book(book , 1) # add a book to the cart

@then("the cart should contain 1 book")
def step_then_check_cart_count(context):
    # This will check the number of books later
    assert context.cart.get_total_books() == 1 , "Expected 1 book, but found {}".format(context.cart.get_total_books())

@then("the total amount should be correct")
def step_then_check_total_amount(context):
    # This will check the total price later
    assert context.cart.get_total_amount() == 10 , "Expected total amount 10, but found {}".format(context.cart.get_total_amount())