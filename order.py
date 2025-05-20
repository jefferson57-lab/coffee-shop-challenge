class Order:
    all_orders = []

    def __init__(self, customer, coffee, price):
        from customer import Customer
        from coffee import Coffee

        if not isinstance(customer, Customer):
            raise TypeError("customer must be an instance of Customer")
        if not isinstance(coffee, Coffee):
            raise TypeError("coffee must be an instance of Coffee")
        if not (isinstance(price, float) or isinstance(price, int)) or not (1.0 <= price <= 10.0):
            raise ValueError("price must be a float between 1.0 and 10.0")

        self._customer = customer
        self._coffee = coffee
        self._price = float(price)

        Order.all_orders.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price
