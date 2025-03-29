from src.user import AuthenticationError

class PaymentError(Exception):
    pass

class Payment:

    def __init__(self, user):
        self.user = user
        self.cart = user.get_cart()
        self.total_amount = self.calculate_total()
        self.payment_method = None
        self.cart_items_snapshot = None

    def calculate_total(self):
        return self.cart.apply_discount()

    def _check_authentication(self):
        # Verifying if user is authenticated
        if not self.user.is_authenticated():
            raise AuthenticationError("User must be logged in.")

    def process_payment(self, payment_method):
        self._check_authentication()

        total = self.cart.apply_discount()
        if total <= 0:
            raise PaymentError("Cart is empty or invalid. Cannot process payment.")

        self.cart_items_snapshot = dict(self.cart.items)
        self.total_amount = total
        self.payment_method = payment_method

        print(f"Payment of {self.total_amount:.2f} SEK using {payment_method} processed successfully.")
        self.cart.empty_cart()

    def generate_receipt(self):
        self._check_authentication()

        if not self.payment_method or not self.cart_items_snapshot:
            raise PaymentError("No payment has been processed yet.")

        original_total = sum(
                                item["quantity"] * item["price"] for item in self.cart_items_snapshot.values()
                            )
        discount_value = original_total - self.total_amount

        receipt_lines = [
            "--- Receipt ---",
            f"User: {self.user.username}",
            f"Payment Method: {self.payment_method}",
            "Items:"
        ]
        for book, details in self.cart_items_snapshot.items():
            line_total = details["quantity"] * details["price"]
            receipt_lines.append(
                f" - {book}: {details['quantity']} x {details['price']} = {line_total:.2f} SEK"
            )
        receipt_lines.extend([
            "",
            f"Subtotal: {original_total:.2f} SEK",
            f"Discount: {discount_value:.2f} SEK",
            f"Total (after discount): {self.total_amount:.2f} SEK",
            "------------------------"
        ])

        return "\n".join(receipt_lines)