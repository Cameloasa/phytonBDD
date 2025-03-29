from src.payment import Payment, PaymentError
from src.user import AuthenticationError, User


def main():
    try:
        # create user
        user = User("user1", "pass123")

        # Login
        user.login("user1", "pass123")
        print("[✓] Login successful.\n")

        # create Cart
        cart = user.get_cart()
        cart.add_book("Book A", 2)
        cart.add_book("Book B", 2)
        print("[✓] Added books to cart.\n")

        # Inițiate payment
        payment = Payment(user)
        payment.process_payment("card")

        # Show recipe
        receipt = payment.generate_receipt()
        print(receipt)


    except AuthenticationError as e:
        print(f"[!] Authentication error: {e}")
    except PaymentError(Exception) as e:
        print(f"[!] Payment error: {e}")
    except Exception as e:
        print(f"[!] Error: {e}")


if __name__ == "__main__":
    main()