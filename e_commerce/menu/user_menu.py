import sys
import os

# Add the project root directory to the sys.path
sys.path.append(
    os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"))
)

from e_commerce.user.user import UserManager


class UserMenu:
    """Display a menu and collects users choices."""

    def __init__(self):
        """Instantiate the UseManager class and provides set of options."""
        self.user_manager = UserManager()
        self.create_choices = {
            "1": self.create_user,
            "2": self.login,
            "3": self.quit,
        }
        self.profile_choices = {
            "1": self.show_profile,
            "2": self.edit_profile,
            "3": self.quit,
        }
        self.edit_profile_choices = {
            "1.": self.change_email,
            "2": self.edit_firstname,
            "3": self.edit_lastname,
            "4": self.change_password,
            "5": self.set_address,
            "6": self.set_phone_number,
            "7": self.delete_account,
            "8": self.quit,
        }

    def display_create_login_menu(self):
        """Display the create and login account menu."""
        print("User Menu\nSelect an option: ")
        print(
            "\t1. Create an account.\n\t2. Already have an account? Login\n\t3. Quit"
        )

    def display_profile(self):
        """Display the user profile menu, for a logged in user."""
        print("Profile Menu\nSelect an option: ")
        print("\t1. Show user Profile \n\t2. Edit profile \n\t3. Quit")

    def display_profile_edit(self):
        """Display the user profile edit menu, for a logged in user."""
        print("Select profile edit option:")
        print(
            "\t1. Change Email\n\t2. Edit first name\n\t3. Edit last name\n\t4. Change password\n\t5. Set/Change Address\n\t6. Set/Change phone number\n\t7. Delete Account\n\t8. Quit"
        )

    def run(self):
        """Display the various menu and respond to user choices."""
        while True:
            if (
                # Checks if there is a current user or the user is logged in to display the appropriate menu.
                not self.user_manager.current_user
                or not self.user_manager.current_user.isLoggedIn
            ):
                self.display_create_login_menu()
                choice = input("Enter Option: ")
                action = self.create_choices.get(choice)
                if action:
                    action()
                else:
                    print("{0} is not a valid option.".format(choice))

            else:
                self.display_profile()
                choice = input("Enter an Option: ")
                action = self.profile_choices.get(choice)
                if action:
                    action()
                else:
                    print("{0} is not a valid option.".format(choice))

            if choice == "2":
                self.edit_profile()
                choice = input("Enter an option: ")
                action = self.edit_profile_choices.get(choice)
                if action:
                    action()
                else:
                    print("{0} is not a valid option.".format(choice))

    def create_user(self):
        """accepts input from users and create a new user."""
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")
        email = input("Enter your email: ")
        password = input("Enter a unique password: ")
        confirm_password = input("Enter password again.")
        result = self.user_manager.create_user(
            first_name, last_name, password, confirm_password, email
        )
        if result == True:
            print("User created successfully.")
        else:
            print(result)

    def login(self):
        """accepts a user inputs and attempts to login the user, if the inputs matches a user's."""
        email = input("Enter your Email: ")
        password = input("Enter your password: ")
        result = self.user_manager.login(email, password)
        if result == True:
            print("Login successfully...")
        else:
            print("password or email does not exit.")

    def show_profile(self):
        """Display the user's profile information."""
        profile = self.user_manager.show_profile()
        print(profile["user"] + " Profile")
        print("\n" + profile["user_info"])

    def change_email(self):
        """accepts a user inputs and set the email to the value."""
        email = input("Enter Email: ")
        self.user_manager.modify_email(email)
        print("Email updated successfully")

    def edit_firstname(self):
        """Updates the usen = UserMenu()
        n.run()r's first name with the provided value"""
        firstname = input("Enter your first name: ")
        self.user_manager.modify_first_name(firstname)
        print("Name updated successfully")

    def edit_lastname(self):
        """updates the user's last name with the provided value"""
        lastname = input("Enter your last name: ")
        self.user_manager.modify_last_name(lastname)
        print("Name updated successfully")

    def change_password(self):
        """Updates the user's password, if the value of the old password is correct."""
        old_password = input("Enter your old password")
        new_password = input("Enter new password.")
        password_update = self.user_manager.change_password(
            old_password, new_password
        )
        if password_update:
            print("Password updated successfully!")
        else:
            print("The old password you entered is not correct!")

    def set_address(self):
        """Set the user's address to the provided value."""
        print("Provide your current address information:\n")
        street = input("Enter your Street: ")
        local_govt = input("Enter your local government: ")
        state = input("Enter your state: ")
        post_code = input("Enter your postal code: ")
        user_address = self.user_manager.set_address(
            street, local_govt, state, post_code
        )
        if user_address:
            print("Address updated successfully!")
        else:
            print("An error occurred! try again.")

    def set_phone_number(self):
        """Set the user's phone number to the provided value."""
        phone_number = input("Enter your phone number:")
        user_phone_number = self.user_manager.modify_phone_number(phone_number)

        if user_phone_number:
            print("Phone number updated successfully!")
        else:
            print("an error occurred, try again!")

    def delete_account(self):
        """Deletes the account of the user. Functionality has not be implemented."""
        print("Are you sure you want to delete your account!!!")

    def quit(self):
        """Terminates the programme."""
        print("Thank your for visiting us today! Bye")
        sys.exit()

    def edit_profile(self):
        self.display_profile_edit()


if __name__ == "__main__":
    menu = UserMenu()
    menu.run()
