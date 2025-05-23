### Camelia Ciuca = https://github.com/Cameloasa/phytonBDD

# Online Bookstore BDD Project

This project uses Behavior-Driven Development (BDD) with Python and Behave to implement an online bookstore system.

## User Story 1 [U1]
**As a** user of the online bookstore,  
**I want to** manage my shopping cart,  
**so that** I can purchase books easily.

### Acceptance Criteria for [U1]
1. The user can add a book to the cart, and the cart reflects the correct number of items.
2. If the user adds multiple copies of the same book, the cart groups them as a single item (e.g., "Book A - 2 copies").
3. The cart calculates the correct total amount after adding a book.

## User Story 2 [U2]
**As a** user of the online bookstore,  
**I want to** receive a discount on my purchases,  
**so that** I can save money when buying multiple books.

### Acceptance Criteria for [U2]
1. The user receives a discount when they buy more than 3 books.
2. The user does not receive a discount if they buy 3 or fewer books.
3. The system prevents invalid quantities (e.g., negative or excessive) from affecting the discount.

## User Story 3 [U3]
**As a** user of the online bookstore,  
**I want to** login to my account,  
**so that** I can have acces to my cart.

### Acceptance Criteria for [U3]
1. Successful Login – The user must be able to log in with a valid email and password.
2. Incorrect Credentials – If the user enters an incorrect email or password, an appropriate error message should be displayed.
3. Session Management – After logging in, the user should remain authenticated until they log out or the session expires.
4. Access to Cart – After logging in, the user should be redirected to their account page with access to their cart.
5. Logout Functionality – The user should be able to log out successfully, which should end their session.

## User Story 4 [U4]
**As a** logged-in user,  
**I want to** login make a payment for my cart,  
**so that** I can complete my purchase and receive a recipe.

### Acceptance Criteria for [U4]
1. The user can process a payment with "card" if logged in and the cart contains items, receiving a confirmation (e.g., "Payment of 45.00 SEK using card processed successfully").
2. The user receives a receipt showing subtotal, discount applied, and total after discount after a successful payment.
3. The cart is emptied after a successful payment.
4. The user receives an error message "User must be logged in to make a payment" if not logged in.
5. The user receives an error message "Cart is empty or invalid. Cannot process payment" if the cart is empty.

