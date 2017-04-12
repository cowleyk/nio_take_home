import json

class Grocerystats:
    # make type parameter into list, loop over in handle_message && display accordingly
    def __init__(self, type):
        self.type = type
        self.total_sales = 0
        self.total_quantity = 0
        self.total_amount = 0
        self.total_male = 0

        self.quantity_obj = {'total': 0}
        for type in type:
            self.quantity_obj[type] = 0
            # print(self.quantity_obj)


    def __repr__(self):
        return 'total sales: {}, total quantity of {}: {} \naverage {}/sale: {}'.format(self.total_sales, self.type, self.total_quantity, self.type, self.total_quantity/self.total_sales)


    def add_sale(self):
        self.total_sales = self.total_sales + 1


    def add_quantity(self, quantity):
        self.total_quantity = self.total_quantity + quantity


    def add_amount(self, amount):
        self.total_amount = self.total_amount + amount


    def calculate_average(self):
        return self.total_quantity/self.total_sales


    def calculate_average_two(self):
        # return self.total_quantity/self.total_sales
        average_of_type_obj = {}
        for label in self.quantity_obj:
            average_of_type_obj[label] = self.quantity_obj[label]/self.total_sales
        return average_of_type_obj


    def calculate_average_amount(self, message, *args):
        # QUESTION: repeating code here, better way to do?  limited by SocketIO 'recvData' structure
        datadict = json.loads(message)

        amount = datadict['amount']
        print('sale amount: {}'.format(amount))

        self.add_sale()
        self.add_amount(amount)

        average_amount = self.total_amount/self.total_sales

        print('average amount: {}'.format(average_amount))
        return average_amount


    def customer_stats(self, message, *args):
        datadict = json.loads(message)
        shopper = datadict['shopper']
        print('shopper: {}'.format(shopper))

        self.add_sale()

        if shopper['gender'] == 'male':
            self.total_male = self.total_male + 1

        # QUESTION: does only tracking one gender save more than negligible space?
        percent_male = (self.total_male/self.total_sales)*100
        percent_female = 100 - percent_male

        print('% male shoppers: {} \n% female shoppers: {}'.format(percent_male, percent_female))


    def handle_message(self, message, *args):
        # create dictionary from socket's JSON string
        datadict = json.loads(message)

        # isolate list of customer order
        cart = datadict['cart']
        # print('message: {}'.format(datadict))

        # increment total sales
        self.add_sale()
        # loop over items and add sum appropriate quantity
        for item in cart:
            if item['type'] == self.type:
                self.add_quantity(item['quantity'])
            else:
                pass

        print(self)
        return self.calculate_average()


    def handle_message_two(self, message, *args):
        datadict = json.loads(message)

        cart = datadict['cart']

        self.add_sale()
        for item in cart:
            if item['type'] in self.type:
                self.quantity_obj[item['type']] = self.quantity_obj[item['type']] + item['quantity']
            else:
                pass

        for type_average in self.calculate_average_two():
            # QUESTION: better memory-wise to just loop over quantity_obj and do quantity/sales inside .format()?
            print('average {} per sale: {}'.format(type_average, self.calculate_average_two()[type_average]))
        print('')
        return self.calculate_average_two()


    def handle_message_two_totals(self, message, *args):
        datadict = json.loads(message)

        cart = datadict['cart']
        print('cart: {}'.format(cart))

        self.add_sale()
        for item in cart:
            if item['type'] in self.type:
                self.quantity_obj['total'] = self.quantity_obj['total'] + item['quantity']
            else:
                pass

        # for type_average in self.calculate_average_two():
        #     print('average {} per sale: {}'.format(type_average, self.calculate_average_two()[type_average]))
        #     can loop inside .format()? want to print; 'average type1, type2, type3... per sale:
        print('average per sale: {}'.format(self.quantity_obj['total']/self.total_sales))
        return self.calculate_average_two()
