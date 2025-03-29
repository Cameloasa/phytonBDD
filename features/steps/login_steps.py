from behave import given, when, then

@given(u'I am on the login page')
def step_on_login_page(context):
    raise NotImplementedError(u'STEP: Given I am on the login page')


@when(u'I enter username "user1" and password "pass123"')
def step_enter_valid_credentials(context):
    raise NotImplementedError(u'STEP: When I enter username "user1" and password "pass123"')


@then(u'I should be logged in successfully')
def step_check_logged_in(context):
    raise NotImplementedError(u'STEP: Then I should be logged in successfully')
