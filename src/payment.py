from src.user import AuthenticationError


class Payment:

    def __init__(self, user):
        self.user = user
        self.cart = user.get_cart()
        self.total_amount = self.calculate_total()
        self.payment_method = None

    def calculate_total(self):
        return self.cart.apply_discount()

    def process_payment(self, payment_method):
        # Verifying if user is authenticate
        if not self.user.is_authenticated():
            raise AuthenticationError("User must be logged in to make a payment.")

        cart = self.user.get_cart()
        self.cart_items_snapshot = dict(cart.items)

        total = cart.apply_discount()

        if total <= 0:
            raise Exception("Cart is empty. Cannot process payment.")

        self.total_amount = total
        self.payment_method = payment_method

        print(f"Payment of {self.total_amount:.2f} SEK using {payment_method} processed successfully.")

        cart.empty_cart()

    def generate_receipt(self):
        if not self.user.is_authenticated():
            raise AuthenticationError("User must be logged in to view receipt.")

        original_total = sum(
            item["quantity"] * item["price"] for item in self.cart_items_snapshot.values()
        )
        discount_value = original_total - self.total_amount

        receipt = f"--- Receipt ---\n"
        receipt += f"User: {self.user.username}\n"
        receipt += f"Payment Method: {self.payment_method}\n"
        receipt += f"Items:\n"

        for book, details in self.cart_items_snapshot.items():
            line_total = details["quantity"] * details["price"]
            receipt += f" - {book}: {details['quantity']} x {details['price']} = {line_total:.2f} SEK\n"

        receipt += f"\nSubtotal: {original_total:.2f} SEK\n"
        receipt += f"Discount: {discount_value:.2f} SEK\n"
        receipt += f"Total (after discount): {self.total_amount:.2f} SEK\n"
        receipt += f"------------------------\n"

        return receipt