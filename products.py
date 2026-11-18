"""Product model for the Best Buy store."""


class Product:
    """A product in the store with name, price, quantity and active status.

    A product becomes inactive when its quantity reaches 0.
    """

    def __init__(self, name, price, quantity):
        """Initialize a product with name, price and quantity.

        Raise ValueError if the name is empty or if price
        or quantity is negative.
        """
        if name == "":
            raise ValueError("The name field cannot be blank")
        self.name = name
        if price < 0:
            raise ValueError("The price field cannot be a negative value")
        self.price = price
        if quantity < 0:
            raise ValueError("The quantity field cannot be a negative value")
        self.quantity = quantity
        self.active = quantity > 0

    def get_quantity(self) -> int:
        """Return the quantity of the product."""
        return self.quantity

    def set_quantity(self, quantity):
        """Set the quantity of the product.

        Deactivate the product if the quantity is less than 1.
        """
        self.quantity = quantity
        if self.quantity < 1:
            self.active = False

    def is_active(self) -> bool:
        """Return True if product is active."""
        return self.active

    def activate(self):
        """Set product to active=True."""
        self.active = True

    def deactivate(self):
        """Set product to active=False."""
        self.active = False

    def show(self):
        """Return the product with price and quantity."""
        return f"{self.name}, Price: {self.price}, Quantity: {self.quantity}"

    def buy(self, quantity) -> float:
        """Buy the given quantity of the product and return the total price.

        Reduce the stock by the bought quantity.
        Raise ValueError if not enough quantity is available.
        """
        if quantity > self.quantity:
            raise ValueError("Not enough quantity")
        self.set_quantity(self.quantity - quantity)
        return float(quantity * self.price)
