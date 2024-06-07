import csv

"""A module that handles operations relating to products."""

class Products:
    """A simple model of a product."""

    all = []

    def __init__(self, name:str, price:int, inventory=0):
        """Initiates the attributes. Then append the instance to the 'all'
        list."""
        assert (
            price >= 0
        ), f"Price {price} is not greater than or equal to zero!"
        assert (
            inventory >= 0
        ), f"Inventory {inventory} is not greater than or equal to zero!"

        self.product_name = name
        self.product_price = price
        self.inventory = inventory
        Products.all.append(self)

    def get_product_info(self):
        """Returns a formatted information about a product."""
        product_info = (
            "\nProducts: "
            + self.product_name
            + "\nPrice: "
            + str(self.product_price)
            + "\nInventory: "
            + str(self.inventory)
        )
        return product_info

    @classmethod
    def instantiate_from_csv(cls):
        """Instantiate data from an csv file."""
        with open("data/product.csv", "r") as f:
            reader = csv.DictReader(f)
            items = list(reader)
            print(items)

            for item in items:
                Products(
                    name=item.get("name"),
                    price=float(item.get("price")),
                    inventory=float(item.get("inventory")),
                )

    def __repr__(self):
        """Returns a string representation of the class instances."""
        return f"{self.__class__.__name__}('{self.product_name}', {self.product_price}, {self.inventory})"


Products.instantiate_from_csv()

print(Products.all)
