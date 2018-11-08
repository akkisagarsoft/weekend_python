class _Computer:
    def __init__(self):
        self.maxPrice = 1000

    def sell(self):
        print("Selling Price: {}".format(self.maxPrice))

    def setMaxPrice(self,price):
        self.maxPrice = price


if __name__ == '__main__':
    comp = _Computer()
    comp.sell()

    # change the price
    comp.maxPrice = 1100
    comp.sell()

    # using setter function
    comp.setMaxPrice(10000)
    comp.sell()