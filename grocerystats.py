import json

class Grocerystats:
    def __init__(self, type):
        self.type = type
        self.total_sales = 0
        self.total_quantity = 0

    def __repr__(self):
        return 'total sales: {}, total quantity of {}: {} \naverage {}/sale: {}'.format(self.total_sales, self.type, self.total_quantity, self.type, self.total_quantity/self.total_sales)

    def add_sale(self):
        self.total_sales = self.total_sales + 1

    def add_quantity(self, quantity):
        self.total_quantity = self.total_quantity + quantity

    def handle_message(self, message, *args):
        # create dictionary from socket's JSON string
        datadict = json.loads(message)

        # isolate list of customer order
        cart = datadict['cart']
        # print('order: {}'.format(cart))

        # increment total sales
        self.add_sale()
        # loop over items and add sum appropriate quantity
        for item in cart:
            if item['type'] == self.type:
                self.add_quantity(item['quantity'])
            else:
                pass

        print(self)


