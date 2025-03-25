class Cart:
    def __init__(self):
        # This will hold the books in the cart
        self.items = {}  # Example: {"Book A": {"quantity": 1, "price": 10}}
        # simulate prices for books
        self.book_prices = {"Book A": 10, "Book B": 15}

    def add_book(self, book_name, quantity):
        # This will add a book to the cart
        if book_name in self.items:
            #if book already exists in items we increase the quantity
            self.items[book_name]["quantity"] += quantity
        else:
            # if is a new book, we add the price
            self.items[book_name] = {"quantity": quantity, "price": self.book_prices[book_name]}

    def get_total_books(self):
        # This will return the total number of books
        total = 0
        for item in self.items.values():
            total += item["quantity"]
        return total

    def get_total_amount(self):
        # This will return the total price
        total = 0
        for item in self.items.values():
            total += item["quantity"] * item["price"]
        return total