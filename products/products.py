class Products:
    """A simple model of a product."""

    def __init__(self, name, price, inventory=1):
        """Initiates the attributes."""
        self.product_name = name
        self.product_price = price
        self.inventory = inventory

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


item_1 = Products("iphone-16", 15, 50)
print(item_1.get_product_info())
