from cart import Cart

class User:

    def __init__(self,username, password):
        self.username = username
        self.password = password
        self.cart = Cart()
        self.logged_in = False # in the beginning is False

    def login(self, username, password):
        if self.username == username and self.password == password:
            self.logged_in = True
            return True
        else:
            raise Exception("Invalid username or password")

    def logout(self):
        logged_in = False

    def is_authenticate(self):
        return self.logged_in

    def get_cart(self):
        if self.logged_in:
            return self.cart
        else:
            raise Exception("User not logged in")



