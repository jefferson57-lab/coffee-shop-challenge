from customer import Customer
from coffee import Coffee
from order import Order

# Create instances
alice = Customer("Alice")
bob = Customer("Bob")

latte = Coffee("Latte")
espresso = Coffee("Espresso")

# Create orders
alice.create_order(latte, 4.5)
bob.create_order(latte, 5.0)
alice.create_order(espresso, 3.0)

# Test relationships
print([order.price for order in latte.orders()])           # [4.5, 5.0]
print([cust.name for cust in latte.customers()])           # ['Alice', 'Bob']
print([coffee.name for coffee in alice.coffees()])         # ['Latte', 'Espresso']
print(latte.num_orders())                                  # 2
print(latte.average_price())                               # 4.75
print(Customer.most_aficionado(latte).name)                # Bob
