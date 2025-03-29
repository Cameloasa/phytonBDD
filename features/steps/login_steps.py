from behave import given, when, then
from src.user import User,AuthenticationError

# Background step
@given('I am on the login page')
def step_on_login_page(context):
    context.user = User(username="user1", password="pass123")

# Common steps for login
@when('I enter username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    try:
        context.user.login(username, password)
    except AuthenticationError as e:
        context.error = e

@then('I should be logged in successfully')
def step_check_logged_in(context):
    assert context.user.is_authenticated()

@then('I should have access to my cart')
def step_check_cart_access(context):
    assert context.user.get_cart() is not None

# Steps for session management
@given('I am logged in as "{username}" with password "{password}"')
def step_already_logged_in(context, username, password):
    context.user.login(username, password)

@when('I refresh the page')
def step_refresh(context):
    pass  # Simulate refresh

@then('I should still be logged in')
def step_check_session(context):
    assert context.user.is_authenticated()

# Steps for logout
@when('I click the logout button')
def step_logout(context):
    context.user.logout()

@then('I should be logged out')
def step_check_logout(context):
    assert not context.user.is_authenticated()

@then('I should not access my cart')
def step_check_no_access(context):
    try:
        context.user.get_cart()
        assert False, "Cart should be inaccessible after logout"
    except AuthenticationError:
        pass

# Steps for error handling
@then('I should see an error "{error_message}"')
def step_check_error(context, error_message):
    assert str(context.error) == error_message

