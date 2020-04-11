class Item:

    def __init__(self, price, discount_strategy=None):
        self._price = price
        self._discount_strategy = discount_strategy

    @property
    def price(self):
        return self._price

    def price_after_discount(self):

        if self._discount_strategy:
            discount = self._discount_strategy(self)
        else:
            discount = 0

        return self._price - discount

    def __repr__(self):
        return f"Price: {self._price}, price after discount: {self.price_after_discount()}"


def on_sale_discount(order):
    """Function dedicated to On Sale Discount"""
    return order.price * 0.25 + 20


def twenty_percent_discount(order):
    """Function dedicated to 20% discount"""
    return order.price * 0.20


if __name__ == "__main__":

    print(Item(20000))

    # With discount strategy as 20 % discount
    print(Item(20000, discount_strategy=twenty_percent_discount))

    # With discount strategy as On Sale Discount
    print(Item(20000, discount_strategy=on_sale_discount))
