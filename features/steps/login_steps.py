from behave import given, when, then
from src.user import User,AuthenticationError

#Step 1. Initialize the user
@given('I am on the login page')
def step_on_login_page(context):
    context.user = User(username="user1", password="pass123")

#Step 2. Enter user credentials and raise exceptions if needed
@when('I enter username "{username}" and password "{password}"')
def step_enter_credentials(context, username, password):
    try:
        context.user.login(username, password)
    except AuthenticationError as e:
        context.error = e

#Step 3. Verifying user successfully logged in
@then('I should be logged in successfully')
def step_check_logged_in(context):
    assert context.user.is_authenticate() is True, "User should be logged in"

# Step 4: Verify error message
@then('I should see an error "{error_message}"')
def step_check_error(context, error_message):
    assert isinstance(context.error, AuthenticationError), "Expected authentication error"
    assert str(context.error) == error_message
