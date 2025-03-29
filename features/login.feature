Feature: User Login
  Scenario: Successful login with valid credentials
    Given I am on the login page
    When I enter username "user1" and password "pass123"
    Then I should be logged in successfully

  Scenario: Failed login with invalid credentials
    Given I am on the login page
    When I enter username "user1" and password "wrongpass"
    Then I should see an error "Invalid username or password"