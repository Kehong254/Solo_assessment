Feature: Testing registration functionality
    As a new user
    I want to be able to register for an account
    So that I can access the site

    Scenario: Successful registration
        Given I am on the registration page
        When I fill in the registration form with valid information
        And I submit the form
        Then I should be redirected to the login page
        And I should see a success message
