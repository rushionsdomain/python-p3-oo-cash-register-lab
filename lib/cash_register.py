class CashRegister:
    def __init__(self, discount=0):
        """Initializes CashRegister with an optional discount, total, and items."""
        self.discount = discount
        self.total = 0
        self.items = []

    def add_item(self, title, price, quantity=1):
        """Adds an item to the register, increasing the total based on price and quantity."""
        self.total += price * quantity
        self.items.extend([title] * quantity)

    def apply_discount(self):
        """Applies the discount to the total price, if any."""
        if self.discount == 0:
            print("There is no discount to apply.")
        else:
            discount_amount = (self.total * self.discount) / 100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${self.total:.2f}.")

    def void_last_transaction(self):
        """Removes the last transaction from the total."""
        if self.items:
            last_item = self.items.pop()
            item_count = self.items.count(last_item) + 1
            price_per_item = self.total / item_count
            self.total -= price_per_item
            if item_count == 1:
                self.items.remove(last_item)
        else:
            print("No transaction to void.")
