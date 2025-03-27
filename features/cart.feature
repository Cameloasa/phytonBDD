Feature: Shopping Cart Management
  As a user of the online bookstore,
  I want to manage my shopping cart,
  so that I can purchase books easily.

  Scenario: Adding different books to the cart
    Given I have an empty cart
    When I add 1 copies of "Book A" to the cart
    And I add 1 copies of "Book B" to the cart
    Then the cart should contain 2 books
    And the total amount should be 25

  Scenario Outline: Adding multiple copies of the same book
    Given I have an empty cart
    When I add <quantity> copies of "<book>" to the cart
    Then the cart should contain <quantity> books
    And the total amount should be <amount>
    And "<book>" should appear as <quantity> copies on one line
    Examples:
      | book    | quantity | amount |
      | Book A  | 1        | 10     |
      | Book A  | 2        | 20     |
      | Book B  | 3        | 45     |

  Scenario Outline: Removing books from the cart
    Given I have a cart with <initial> copies of "<book>"
    When I remove <remove> copies of "<book>" from the cart
    Then the cart should contain <remaining> books
    And the total amount should be <amount>
    Examples:
      | book    | initial | remove | remaining | amount |
      | Book A  | 2       | 1      | 1         | 10     |
      | Book B  | 3       | 2      | 1         | 15     |
      | Book A  | 1       | 1      | 0         | 0      |

  Scenario: Emptying the cart
    Given I have a cart with 1 copy of "Book A" and 1 copy of "Book B"
    When I empty the cart
    Then the cart should contain 0 books
    And the total amount should be 0