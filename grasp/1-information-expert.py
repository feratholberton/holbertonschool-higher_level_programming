class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price


class LineItem:
  def __init__(self, product: Product, quantity: int):
    self.product = product
    self.quantity = quantity

  def subtotal(self):
    return self.product.price * self.quantity


class Cart:
  def __init__(self):
    self.items = []

  def add_item(self, product, quantity):
    self.items.append(LineItem(product, quantity))

  def total(self):
    return sum(item.subtotal() for item in self.items)
  
  def print_receipt(self):
    print("\n--- Your Receipt ---")
    for item in self.items:
      print(f'{item.quantity} x {item.product.name} @ ${item.product.price:.2f} = ${item.subtotal():.2f}')
    print(f'Total: ${self.total():.2f}')
    print("--------------------")


def main():
    # Step 1: Fruit catalog
    fruits = [
        Product("Apple", 0.5),
        Product("Banana", 0.3),
        Product("Orange", 0.7),
        Product("Grapes", 2.0),
        Product("Watermelon", 4.0),
        Product("Strawberry", 1.5),
    ]

    cart = Cart()

    while True:
        print("\n--- Welcome to the Fruit Shop ---")
        for i, fruit in enumerate(fruits, start=1):
            print(f"{i}. {fruit.name} - ${fruit.price:.2f}")

        choice = input("Enter the number of the fruit to add to your cart (or 'done' to finish): ")

        if choice.lower() == 'done':
            break

        if not choice.isdigit() or not (1 <= int(choice) <= len(fruits)):
            print("Invalid choice. Try again.")
            continue

        selected_fruit = fruits[int(choice) - 1]
        qty_input = input(f"How many {selected_fruit.name}s would you like to buy? ")

        if not qty_input.isdigit() or int(qty_input) <= 0:
            print("Invalid quantity. Try again.")
            continue

        quantity = int(qty_input)
        cart.add_item(selected_fruit, quantity)
        print(f"Added {quantity} x {selected_fruit.name} to your cart.")

    cart.print_receipt()


# Run the fruit shop
if __name__ == "__main__":
    main()