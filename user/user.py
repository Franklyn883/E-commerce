from address import Address


class User:
    """A simple attempt to model a user."""

    users = []

    def __init__(self):
        """Initiates the class attributes. Then Instantiate the Address class."""
        self.user_address = Address()
        self.isLoggedIn = False

    def register_user(
        self, first_name, last_name, email, address, phone_number=""
    ):
        """Register a new user. And add the newly register user to the users
        list."""

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.phone_number = phone_number

        User.users.append(self)

    def login(self):
        """Set the IsloggedIn attribute to True."""
        self.isLoggedIn = True

    def logout(self):
        """Set the IsloggedIn attribute to False."""
        self.isLoggedIn = False

    def get_full_name(self):
        """Returns the first_and and the last_name of the user object."""
        full_name = self.first_name + " " + self.last_name
        return full_name.title()

    def get_users(self):
        """Returns the full names of users all the registered users."""
        print("list of users:")
        for user in User.users:

            print("\t" + user.get_full_name())

    def get_number_of_users(self):
        """Returns the number of users registered users."""
        return len(User.users)


new_user = User()
user_2 = User()
user_2.register_user(
    first_name="favor",
    last_name="Iyoha",
    address=user_2.user_address.set_address(
        state="edo",
        local_govt="oredo",
        street="no 6a, ohonre street",
        post_code="4556",
    ),
    email="favorgodwin@gmail.com",
    phone_number="08163953883",
)
new_user.register_user(
    "frank", "alimimian", "frankyngood@gmail.com", "edo state."
)
print(new_user.__dict__)
print(new_user.get_full_name())
new_user.get_users()
print(new_user.get_number_of_users())
address_info = user_2.user_address.get_full_address()
print(address_info)
print(user_2.isLoggedIn)
user_2.login()
print(user_2.isLoggedIn)