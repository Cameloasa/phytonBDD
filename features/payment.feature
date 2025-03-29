Feature: Payment Processing and Receipt Generation
  As a logged-in user
  I want to make a payment for my cart
  So that I can complete my purchase and receive a receipt

  Background:
    Given I am logged in as "user1" with password "pass123"
    And my cart contains:
      | Book   | Quantity |
      | Book A | 2        |
      | Book B | 2        |

  # -------------------------------
  # 1: Successful payment
  # -------------------------------
  Scenario: Successfully process payment and generate receipt
    When I choose to pay using "card"
    Then the payment should be processed
    And I should receive a receipt with:
      | Subtotal            | 50.00  |
      | Discount Applied    | 5.00   |
      | Total After Discount| 45.00  |
    And my cart should be empty

  # -------------------------------
  # 2: Try payment without login
  # -------------------------------
  Scenario: Attempt payment while not logged in
    Given I am not logged in
    When I try to pay using "card"
    Then I should see an error "User must be logged in to make a payment"

  # -------------------------------
  # 3: Try payment with empty cart
  # -------------------------------
  Scenario: Attempt payment with empty cart
    Given I am logged in as "user1" with password "pass123"
    And my cart is empty
    When I try to pay using "card"
    Then I should see an error "Cart is empty. Cannot process payment."