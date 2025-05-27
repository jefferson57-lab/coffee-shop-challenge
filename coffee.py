class Coffee:
    def __init__(self, name):

        if not isinstance(name, str) or len(name) < 3:
            raise ValueError(
                "name should be a string and greater than or equal to 3 chars")
        self._name = name

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise AttributeError('coffee name cannot be changed')

    def orders(self):
        from order import Order
        return [order for order in Order.all() if order.coffee == self]

    def customers(self):
        from order import Order
        return list({order.customer for order in self.orders()})

    def num_orders(self):
        return len(self.orders())

    def average_price(self):
        prices = [order.price for order in self.orders()]
        return sum(prices) / len(prices) if prices else 0