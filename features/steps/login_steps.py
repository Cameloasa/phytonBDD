from behave import given, when, then
from user import User,AuthenticationError


@given(u'I am on the login page')
def step_on_login_page(context, username, password):
    context.user = User(username="user1", password="pass123")

@when(u'I enter {username} and {password}')
def step_enter_valid_credentials(context,username, password):
    try:
        context.user.login(username,password)
    except AuthenticationError:
        context.error = str(e)

@then(u'I should be logged in successfully')
def step_check_logged_in(context):
    assert context.user.is_authenticate() is True, "User should be logged in"

@then('I should see an error "{error_message}"')
def step_check_error(context, error_message):
    assert context.error == error_message, f"Expected error: {error_message}"
