
from behave import when, then

@when('I apply the discount')
def step_when_apply_discount(context):
    context.total_with_discount = context.cart.apply_discount()

@then('I should see an error message "{message}"')
def step_then_check_error(context, message):
    assert hasattr(context, "error"), "No error occurred"
    assert context.error == message, f"Expected error '{message}', but got '{context.error}'"