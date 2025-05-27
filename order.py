from customer import Customer
from coffee import Coffee


class Order:

    _all = []

    def __init__(self, customer, coffee, price):
        if not isinstance(customer, Customer):
            raise TypeError('must be a Customer instance!')
        if not isinstance(coffee, Coffee):
            raise TypeError('must be a Coffee instance!')
        if not isinstance(price, float) or not (1.0 <= price <= 10.0):
            raise ValueError("Must be a float between 1.0 and 10.0")

        self._coffee = coffee
        self._customer = customer
        self._price = price
        Order._all.append(self)

    @property
    def customer(self):
        return self._customer

    @property
    def coffee(self):
        return self._coffee

    @property
    def price(self):
        return self._price

    @classmethod
    def all(cls):
        return cls._all