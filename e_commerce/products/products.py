class Category:
    """Model of category."""

    last_id = 0

    def __init__(self, name):
        """Initialize the class properties."""
        self.name = name
        self.last_id += 1
        self.id = self.last_id


class Product:
    """Model of a product."""

    last_id = 0

    def __init__(self, name, price, quantity, category, **kwargs):
        """Initializes the attributes of the class."""

        self.name = name
        self.price = price
        self.quantity = quantity
        self.category = category

        self.last_id += 1
        self.id = self.last_id
        self.kwargs = kwargs

    def update_quantity(self, num):
        """Update the quantity."""
        self.quantity += num


class Inventory:
    """A model for an inventory."""

    def __init__(self):
        """Initialize the properties of the class."""
        self.products = []
        self.categories = []

    def add_category(self, category):
        """Adds a category to the category list."""
        self.categories.append(category)

    def add_product(self, product):
        """Adds a product to the products list."""
        self.products.append(product)

    def find_product(self, filter):
        """Finds a product, using the name."""
        filter = filter.lower()
        products = []
        for product in self.products:
            
            if filter in product.name.lower():
                print(product.name)
                products.append(product)

        return products
    
    def __str__(self):
        return '\n'.join([str(product) for product in self.products])


class Cart:
    """A cart model."""

    def __init__(self):
        """Initialize the class properties."""
        self.user = None
        self.items = []

    def add_product(self, product, quantity):
        """Adds product to cart."""
        if product.quantity >= quantity:
            self.items.append(product, quantity)
            product.update_quantity(-quantity)

        else:
            print("Not enough stock for product {}.".format(product.name))

    def total_cost(self):
        """returns the total price for the products."""
        return sum(product.price * quantity for product, quantity in self.items)

    def checkout(self):
        """Checkout the products."""
        total = self.total_cost()
        self.items = []  # Empty the cart after checkout
        return total

    # Create categories


electronics = Category("Electronics")
home_appliances = Category("Home Appliances")
furniture = Category("Furniture")
books = Category("Books")
clothing = Category("Clothing")

# Create an inventory
inventory = Inventory()

# Add categories to the inventory
inventory.add_category(electronics)
inventory.add_category(home_appliances)
inventory.add_category(furniture)
inventory.add_category(books)
inventory.add_category(clothing)

# Add products to the inventory with extra attributes
inventory.add_product(
    Product(
        "Laptop",
        999.99,
        10,
        electronics,
        brand="Dell",
        model="XPS 13",
        warranty="2 years",
    )
)
inventory.add_product(
    Product(
        "Smartphone",
        799.99,
        20,
        electronics,
        brand="Apple",
        model="iPhone 13",
        warranty="1 year",
        color="Black",
    )
)
inventory.add_product(
    Product(
        "Smartphone",
        799.99,
        20,
        electronics,
        brand="Samsung",
        model="S23",
        warranty="1 year",
        color="Black",
    )
)
inventory.add_product(
    Product(
        "Microwave",
        150.00,
        5,
        home_appliances,
        brand="Panasonic",
        model="NN-SN966S",
        power="1250W",
    )
)
inventory.add_product(
    Product(
        "Refrigerator",
        1200.00,
        3,
        home_appliances,
        brand="LG",
        model="LFXS26973S",
        capacity="500L",
    )
)
inventory.add_product(
    Product(
        "Sofa",
        399.99,
        15,
        furniture,
        brand="IKEA",
        model="EKTORP",
        material="Fabric",
    )
)
inventory.add_product(
    Product(
        "Dining Table",
        299.99,
        10,
        furniture,
        brand="Ashley Furniture",
        model="Whitesburg",
        material="Wood",
    )
)
inventory.add_product(
    Product(
        "Fiction Book",
        10.99,
        100,
        books,
        title="The Great Gatsby",
        author="F. Scott Fitzgerald",
        ISBN="978-0743273565",
    )
)
inventory.add_product(
    Product(
        "Non-Fiction Book",
        14.99,
        50,
        books,
        title="Sapiens: A Brief History of Humankind",
        author="Yuval Noah Harari",
        ISBN="978-0062316097",
    )
)
inventory.add_product(
    Product(
        "T-Shirt",
        25.00,
        200,
        clothing,
        brand="Nike",
        model="Dri-FIT",
        size="M",
    )
)
inventory.add_product(
    Product(
        "Jeans",
        49.99,
        150,
        clothing,
        brand="Levi's",
        model="501 Original Fit",
        size="32",
    )
)
print(inventory.find_product('smart'))
#print([ [product.name,product.price,product.quantity,product.category.name] for product in inventory.products])