class ShoppingCart:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)
        print(f"{item} added to the cart.")

    def remove_item(self, item_name):
        if item_name in self.items:
            self.items.remove(item_name)
            print(f"{item_name} removed from the cart.")

        else:
            print(f"Item with name {item_name} not found in the cart.")

    def display_items(self):
        print(f"items in the cart:\n{self.items}")

shoping_cart=ShoppingCart()
shoping_cart.add_item("apple")
shoping_cart.display_items()





