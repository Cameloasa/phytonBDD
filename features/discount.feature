Feature: Discount Application
  As a user of the online bookstore,
  I want to receive a discount on my purchases,
  so that I can save money when buying multiple books.

  Scenario: Applying 10% discount when buying more than 3 books
    Given I have an empty cart
    When I add 4 copies of "Book A" to the cart
    And I apply the discount
    Then the total amount should be 36

  Scenario: No discount when buying 3 or less books
    Given I have an empty cart
    When I add 3 copies of "Book A" to the cart
    And I apply the discount
    Then the toTal amount should be 30

   Scenario: Handling negative total amount
    Given I have an empty cart
    When I add -10000 copies of "Book A" to the cart
    And I apply the discount
    Then I should see an error message "Invalid cart quantity"

   Scenario: Handling excessive book quantity
    Given I have an empty cart
    When I add 50000 copies of "Book A" to the cart
    And I apply the discount
    Then I should see an error message "Quantity exceeds available stock"

