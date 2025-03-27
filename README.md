### Camelia Ciuca = https://github.com/Cameloasa/phytonBDD

# Online Bookstore BDD Project

This project uses Behavior-Driven Development (BDD) with Python and Behave to implement an online bookstore system.

## User Story 1 [U1]
**As a** user of the online bookstore,  
**I want to** manage my shopping cart,  
**so that** I can purchase books easily.

### Acceptance Criteria
1. The user can add a book to the cart, and the cart reflects the correct number of items.
2. If the user adds multiple copies of the same book, the cart groups them as a single item (e.g., "Book A - 2 copies").
3. The cart calculates the correct total amount after adding a book.

## User Story 2 [U2]
**As a** user of the online bookstore,  
**I want to** receive a discount on my purchases,  
**so that** I can save money when buying multiple books.

### Acceptance Criteria
1. The user receives a discount when they buy more than 3 books.
2. The user does not receive a discount if they buy 3 or fewer books.
3. The system prevents invalid quantities (e.g., negative or excessive) from affecting the discount.

