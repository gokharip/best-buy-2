"""Store model for the Best Buy store."""

from products import Product


class Store:
    """A store that holds a list of products and processes orders."""

    def __init__(self, product_list):
        """Initialize the store with a list of products."""
        self.product_list = product_list

    def add_product(self, product):
        """Add a product to the store."""
        self.product_list.append(product)

    def remove_product(self, product):
        """Remove a product from the store.

        Raise ValueError if the product is not in the store.
        """
        self.product_list.remove(product)

    def get_total_quantity(self) -> int:
        """Return the total quantity of all products in the store."""
        total = 0
        for product in self.product_list:
            total += product.get_quantity()
        return total

    def get_all_products(self) -> list[Product]:
        """Return all active products in the store."""
        active_products = []
        for product in self.product_list:
            if product.is_active():
                active_products.append(product)
        return active_products

    @staticmethod
    def order(shopping_list) -> float:
        """Buy all products in the shopping list and return the total price.

                The shopping list contains (product, quantity) tuples.
                Raise ValueError if a product does not have enough quantity.
                """
        total_price = 0
        for product, quantity in shopping_list:
            total_price += product.buy(quantity)
        return total_price
