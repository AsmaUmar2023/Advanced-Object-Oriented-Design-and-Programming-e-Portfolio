
from abc import ABC, abstractmethod


# 1. Product class
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# 2. SRP: Manages shopping cart and calculates total
class Order:
    def __init__(self):
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.price for item in self.items)


# 3. SRP: Handles discount calculations
class Discount:
    def apply_discount(self, total, percentage):
        if not 0 <= percentage <= 100:
            raise ValueError("Discount must be between 0 and 100.")

        return total * (1 - percentage / 100)


# 4. OCP and DIP: Payment abstraction
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# 5. Different payment methods
class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid £{amount:.2f} using Credit Card.")


class PayPalPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid £{amount:.2f} using PayPal.")


class CryptoPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid £{amount:.2f} using Cryptocurrency.")


# 6. SRP and DIP: Processes payments
class PaymentProcessor:
    def process_payment(self, payment_method, amount):
        payment_method.pay(amount)


# 7. Main shopping system
order = Order()

# Add products to shopping cart
order.add_item(Item("Book", 20))
order.add_item(Item("Pen", 5))

# Calculate total price
total = order.calculate_total()

print("----- ONLINE SHOPPING SYSTEM -----")
print(f"Book: £20.00")
print(f"Pen: £5.00")
print(f"Original total: £{total:.2f}")

# Apply 10% discount
discount = Discount()
final_total = discount.apply_discount(total, 10)

print(f"Total after 10% discount: £{final_total:.2f}")

# Process payment
processor = PaymentProcessor()

payment = CreditCardPayment()
processor.process_payment(payment, final_total)

payment = PayPalPayment()
processor.process_payment(payment, final_total)

payment = CryptoPayment()
processor.process_payment(payment, final_total)
