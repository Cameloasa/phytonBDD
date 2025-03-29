from src.cart import Cart

class User:

    def __init__(self,username, password):
        self.username = username
        self.password = password
        self.cart = Cart()
        self.logged_in = False # in the beginning is False

    def login(self, username, password):
        if self.logged_in:
            raise AuthenticationError("Already logged in")
        if self.username == username and self.password == password:
            self.logged_in = True
            return True
        raise AuthenticationError("Invalid username or password")

    def logout(self):
        self.logged_in = False

    def is_authenticated(self):
        return self.logged_in

    def get_cart(self):
        if not self.logged_in:
            raise AuthenticationError("User not logged in")
        return self.cart

class AuthenticationError(Exception):
    pass

