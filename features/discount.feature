Feature: Discount Application
    As a user of the online bookstore,
    I want to receive discount on my purchase
    so that I can save money when buying multiple books.

    Scenario: Applying 10% discount when buying more than 3 books
        Given I have an empty cart
        When I add 4 copies of "Book A"
        And I apply the discount
        Then the total amount should be 36

