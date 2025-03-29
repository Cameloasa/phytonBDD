Feature: User Authentication and Session Management
  As a user
  I want to log in, access my cart, and log out
  So that I can manage my account securely

  Background:
    Given I am on the login page

  # -------------------------------
  # 1: Successfully login
  # -------------------------------
  Scenario: Successful login with valid credentials
    When I enter username "user1" and password "pass123"
    Then I should be logged in successfully
    And I should have access to my cart

  # -------------------------------
  # 2: Failed login with wrong credentials
  # -------------------------------
  Scenario: Failed login with invalid password
    When I enter username "user1" and password "wrongpass"
    Then I should see an error "Invalid username or password"

  # -------------------------------
  # 3: Session Management
  # -------------------------------
  Scenario: Session remains active after login
    Given I am logged in as "user1" with password "pass123"
    When I refresh the page
    Then I should still be logged in

  # -------------------------------
  # 5: Logout
  # -------------------------------
  Scenario: User logs out successfully
    Given I am logged in as "user1" with password "pass123"
    When I click the logout button
    Then I should be logged out
    And I should not access my cart
