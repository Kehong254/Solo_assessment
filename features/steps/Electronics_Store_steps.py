from behave import given, when, then

@given('I am on the registration page')
def step_impl(context):
    context.browser.get(context.base_url + '/register')

@when('I fill in the registration form with valid information')
def step_impl(context):
    context.browser.find_element_by_name('username').send_keys('testuser')
    context.browser.find_element_by_name('email').send_keys('testuser@example.com')
    context.browser.find_element_by_name('password1').send_keys('testpassword')
    context.browser.find_element_by_name('password2').send_keys('testpassword')

@when('I submit the form')
def step_impl(context):
    context.browser.find_element_by_name('submit').click()

@then('I should be redirected to the login page')
def step_impl(context):
    assert context.browser.current_url == context.base_url + '/login'

@then('I should see a success message')
def step_impl(context):
    assert 'Registration successful' in context.browser.page_source

