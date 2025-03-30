from src.user import AuthenticationError

class PaymentError(Exception):
    pass

class Payment:
    def __init__(self, user):
        self.user = user
        self.cart = user.get_cart()
        self.total_amount = 0
        self.payment_method = None
        self.cart_items_snapshot = {}
        self.confirmation_message = None

    def _check_authentication(self):
        if not self.user.is_authenticated():
            raise AuthenticationError("User must be logged in to make a payment")

    def process_payment(self, payment_method):
        self._check_authentication()
        total = self.cart.apply_discount()
        if total <= 0:
            raise PaymentError("Cart is empty or invalid. Cannot process payment.")
        self.cart_items_snapshot = dict(self.cart.items)
        self.total_amount = total
        self.payment_method = payment_method
        self.confirmation_message = f"Payment of {self.total_amount:.2f} SEK using {payment_method} processed successfully."
        print(self.confirmation_message)
        self.cart.empty_cart()

    def generate_receipt(self):
        receipt = "Receipt:\n"
        for item, details in self.cart_items_snapshot.items():
            qty = details["quantity"]
            price = details["price"]
            receipt += f"{item}: {qty} x {price} SEK\n"
        subtotal = sum(details["quantity"] * details["price"] for details in self.cart_items_snapshot.values())
        receipt += f"Subtotal: {subtotal:.2f} SEK\n"
        receipt += f"Discount: {(subtotal - self.total_amount):.2f} SEK\n"
        receipt += f"Total (after discount): {self.total_amount:.2f} SEK"
        return receipt