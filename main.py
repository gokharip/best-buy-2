"""Command-line menu for the Best Buy store."""

from products import Product
from store import Store


def start(store):
    """Show the store menu and handle the user's choice until quit."""
    while True:
        print("\n   Store Menu")
        print("   ----------")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Please choose a number: ")

        if choice == "1":
            list_all_products(store.get_all_products())

        elif choice == "2":
            show_total_amount(store.get_total_quantity())

        elif choice == "3":
            make_order(store)

        elif choice == "4":
            break

        else:
            print("Error with your choice! Try again!")


def list_all_products(all_products):
    """Print a numbered list of the given products."""
    print("----------")
    for number, product in enumerate(all_products, start=1):
        print(f"{number}. {product.show()}")
    print("----------")


def show_total_amount(total_quantity):
    """Print the total quantity of items in the store."""
    print(f"Total of {total_quantity} items in store")


def make_order(store):
    """Let the user build a shopping list and place the order.

    Ask for product numbers and amounts until the user enters
    empty text. Invalid input is rejected with a message.
    """
    all_products = store.get_all_products()
    shopping_list = []
    for number, product in enumerate(all_products, start=1):
        print(f"{number}. {product.show()}")
    print("----------")
    print("When you want to finish order, enter empty text.")
    while True:
        while True:
            product_number = input("Which product # do you want?: ")
            try:
                if (product_number == ""
                        or 0 < int(product_number) <= len(all_products)):
                    break
            except ValueError:
                print("Please enter a valid number.")
                continue
            print("Product number not found. "
                  "Please select a valid product number.")

        if product_number == "":
            break

        product = all_products[int(product_number) - 1]

        while True:
            amount = input("What amount do you want?: ")
            try:
                if amount == "" or 0 < int(amount) <= product.get_quantity():
                    break
            except ValueError:
                print("Please enter a valid number.")
                continue
            if int(amount) <= 0:
                print("Amount must be greater than 0.")
            else:
                print("Not enough stock. "
                      f"Only {product.get_quantity()} available.")
        if amount == "":
            break

        shopping_list.append((product, int(amount)))
        print("Product added to list!\n")

    if shopping_list:
        total_price = store.order(shopping_list)
        print("********")
        print(f"Order made! Total payment: ${total_price}")


def main():
    """Create the store with its products and start the menu."""
    product_list = [
        Product("MacBook Air M2", price=1450, quantity=100),
        Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()
