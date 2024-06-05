class Address:
    """A simple model of users address."""

    def set_address(self, street, local_govt, state, post_code):
        """Set the values of the attributes."""
        self.street = street
        self.local_govt = local_govt
        self.state = state
        self.postal_code = post_code

    def get_full_address(self):
        """Returns a formatted full address."""
        full_address = (
            "\tStreet: "
            + self.street
            + "\n\tLocal government area: "
            + self.local_govt.title()
            + "\n\tState: "
            + self.state.title()
            + "\n\tPostal code: "
            + self.postal_code
        )

        return full_address
