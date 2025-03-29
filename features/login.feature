Feature: User Login
  As a user of the online bookstore,
  I want to log in to my account,
  so that I can access my cart and personal offers.

  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter username "user1" and password "pass123"
    Then I should be logged in successfully