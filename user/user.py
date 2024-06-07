from address import Address
import datetime


def set_user_address(user, street, local_govt, state, post_code):
    """Set the user's address using the Address class."""
    user.address = Address()
    user.address.set_address(street, local_govt, state, post_code)


last_id = 0


class User:
    """A simple attempt to model a user."""

    def __init__(
        self, first_name, last_name, email, address, phone_number, password
    ):
        """Initiates the class attributes. Then Instantiate the Address class."""
        self.isLoggedIn = False
        global last_id
        last_id = +last_id
        self.id = last_id
        self.created_at = datetime.date.today()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.address = address
        self.phone_number = phone_number
        self.password = password

    def match(self, filter):
        """Determines if a user's attributes matches the filter text.
        Returns true if a match is found and false if not found.
        It's case insensitive."""
        filter = filter.lower()

        return (
            filter in self.first_name.lower()
            or filter in self.last_name.lower()
            or filter in self.email.lower()
        )

    def get_full_name(self):
        """Returns the first_and and the last_name of the user object."""
        full_name = self.first_name + " " + self.last_name
        return full_name.title()


class UserManager:
    """Represent a collections of users. It handles user creation and
    modification."""

    def __init__(self):
        """Initialize a list of users."""

        self.users = []
        self.current_user = None

    def create_user(
        self,
        first_name,
        last_name,
        password,
        confirm_password,
        phone_number=None,
        email=None,
        address=None,
    ):
        """Creates a new user. Checks if the password matches the confirm password before adding to list."""
        if password == confirm_password:
            user = User(
                first_name, last_name, email, phone_number, address, password
            )
            self.users.append(user)
        else:
            return "Password and confirm password does not match."

    def login(self, email, password):
        """Logs in user if the password and email matches. 
        Then set the current user to the user."""

        for user in self.users:
            if user.email == email and user.password == password:
                user.isLoggedIn = True
                self.current_user = user
                return True
            return False

    def _find_user(self, user_id):
        """Searches for a user with a given id."""
        for user in self.users:
            if str(user_id) == str(user.id):
                return user
        return None

    def modify_first_name(self, first_name, user_id):
        """Find a user with the given id and replace the first_name with
        the given value"""
        user = self._find_user(user_id)
        if user:
            user.first_name = first_name
            return True
        return False

    def modify_last_name(self, last_name, user_id):
        """Find a user with the given id and replace the last_name with
        the given value"""
        user = self._find_user(user_id)
        if user:
            user.last_name = last_name
            return True
        return False

    def modify_last_name(self, last_name, user_id):
        """Find a user with the given id and replace the last_name with
        the given value"""
        user = self._find_user(user_id)
        if user:
            user.last_name = last_name
            return True
        return False
