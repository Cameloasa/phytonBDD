Feature: Adding books to the shopping cart
  As a user of the online bookstore,
  I want to add books to my cart,
  so that I can purchase them later.

  Scenario: Adding one book to an empty cart
    Given I have an empty cart
    When I add 1 copy of "Book A" to the cart
    Then the cart should contain 1 book
    And the total amount should be correct

  Scenario: Adding two copies of the same book
    Given I have an empty cart
    When I add 2 copies of "Book A" to the cart
    Then the cart should contain 2 books
    And the total amount should be 20