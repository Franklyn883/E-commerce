import sys
import os

# Add the project root directory to the sys.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
)

from e_commerce.user.address import Address
import datetime


def set_user_address(user, street, local_govt, state, post_code):
    """Instantiate the Address class, and set the given user's address using the Address class."""
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
        self.user_id = last_id
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
    modification and other actions relating to the user class."""

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
        email,
        phone_number=None,
        address=None
    ):
        """Creates a new user. Checks if the password matches the confirm password before adding to list. And also if the email exits"""

        for user in self.users:
            if user.email == email:
                return "Email already exists!"

        if password != confirm_password:
            return "Password and confirm password do not match."

        new_user = User(
            first_name,
            last_name,
            email,
            phone_number,
            address,
            password,
        )
        self.users.append(new_user)
        return True

    def login(self, email, password):
        """Logs in user if the password and email matches any of the password and email in the user collection.
        Then set the  user as the current_user."""

        for user in self.users:
            if user.email == email and user.password == password:
                user.isLoggedIn = True
                self.current_user = user
                return True
            return False

    def show_profile(self):
        """Display a user's information in a formatted strings."""
        user = None
        user_info = None

        if self.current_user and self.current_user.isLoggedIn:
            user = self.current_user.get_full_name()
            user_info = ("\tFirst Name : {0}\n\tLast Name: {1}\n\tDate join: {2}\n").format(
                self.current_user.first_name.title(),
                self.current_user.last_name.title(),
                self.current_user.created_at
            )

            if self.current_user.email:
                user_info += "\n\tEmail: {0}".format(
                    self.current_user.email
                )
            if self.current_user.phone_number:
                user_info += "\n\tPhone Number: {0}\n".format(
                    self.current_user.phone_number
                )
            if self.current_user.address:
                user_info += "\n\tAddress: \n\t\tStreet: {0}\n\t\tL.G.A: {1}\n\t\tState: {2}\n\t\tPostal Code: {3}\n".format(
                    self.current_user.address.street.title(),
                    self.current_user.address.local_govt.title(),
                    self.current_user.address.state.title(),
                    self.current_user.address.postal_code,
                )
        return {"user": user, "user_info": user_info}

    def logout(self):
        """Logs out the current user. Then reset the current user to none."""
        if self.current_user:
            self.current_user.isLoggedIn = False
            self.current_user = None

    def modify_first_name(self, first_name):
        """Modify the first_name of the current logged in user."""
        if self.current_user and self.current_user.isLoggedIn:
            self.current_user.first_name = first_name
            return True
        return False

    def modify_last_name(self, last_name):
        """Modify the last_name of the current logged in user."""
        if self.current_user and self.current_user.isLoggedIn:
            self.current_user.last_name = last_name
            return True
        return False

    def modify_email(self, email):
        """Modify the email of the current logged in user."""
        if self.current_user and self.current_user.isLoggedIn:
            self.current_user.email = email
            return True
        return False

    def modify_phone_number(self, phone_number):
        """Modify the phone_number of the current logged in user."""
        if self.current_user and self.current_user.isLoggedIn:
            self.current_user.phone_number = phone_number
            return True
        return False

    def change_password(self, new_password, old_password):
        """Change the password of the current user, if the old password matches with the new password, then return True, return False otherwise."""

        if self.current_user and self.current_user.isLoggedIn:
            if self.current_user.password == old_password:
                self.current_user.password = new_password
                return True
        return False

    def set_address(self, street, local_govt, state, post_code):
        """Set the user's address, and return True."""
        if self.current_user and self.current_user.isLoggedIn:
            user = self.current_user
            set_user_address(user, street, local_govt, state, post_code)
            return True
        return False


if __name__ == "__main__":
    n = UserManager()
    n.create_user(
        first_name="frank",
        last_name="alimimian",
        email="frankalimimian@gmail.com",
        confirm_password="frank123",
        password="frank123",
    )

    print(n.users)
    for user in n.users:
        print(user.email)
    print(n.current_user)
    print(n.login(email="frankalimimian@gmail.com", password="frank123"))
    n.set_address(
        street="9, ohonre street",
        local_govt="Oredeo",
        state="Edo",
        post_code="1234",
    )
    print(n.current_user.address.street)
    print(n.current_user.first_name)
