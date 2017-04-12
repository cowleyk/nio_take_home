from grocerystats import Grocerystats
import unittest
import json


class GrocerystatsTest(unittest.TestCase):

    # test class creation
    def test_create_grocery(self):
        grocery = Grocerystats('vegetable')
        self.assertEqual(grocery.type, 'vegetable')
        self.assertEqual(grocery.total_sales, 0)
        self.assertEqual(grocery.total_quantity, 0)

    # test add_sale method
    def test_add_sale(self):
        grocery = Grocerystats('fruit')
        grocery.add_sale()
        grocery.add_sale()

        self.assertEqual(grocery.total_sales, 2)

    # test add_quantity method
    def test_add_quantity(self):
        grocery = Grocerystats('fruit')
        grocery.add_quantity(1)
        grocery.add_quantity(1)

        self.assertEqual(grocery.total_quantity, 2)

    # test calculate_average method
    def test_calculate_average(self):
        grocery = Grocerystats('fruit')
        grocery.add_quantity(1)
        grocery.add_quantity(1)
        grocery.add_quantity(1)
        grocery.add_quantity(1)
        grocery.add_sale()
        grocery.add_sale()

        self.assertEqual(grocery.calculate_average(), 2)

    # not testing message string to json conversion, assuming json.loads() works

    # test 'cart' isolation
    # QUESTION: Is this too granular of a test?
    def test_cart_isolation(self):

        # from sample data in problem's .pdf
        message_json = {
            "shopper": {
                "name": "John Smith",
                "gender": "male"
            },
            "amount": 47.12,
            "cart": [
                {
                    "name": "apple",
                    "type": "fruit",
                    "quantity": 3
                }, {
                }]
        }

        self.assertEqual(message_json['cart'], [{"name": "apple",
                    "type": "fruit",
                    "quantity": 3}, {}])

    def test_handle_message(self):
        message = {"shopper": {"name": "John Smith","gender": "male"},"amount": 47.12,"cart": [{"name": "apple","type": "fruit","quantity": 4}, {"name": "orange","type": "fruit","quantity": 2}]}
        messagetwo = {"shopper": {"name": "John Smith","gender": "male"},"amount": 47.12,"cart": [{"name": "apple","type": "fruit","quantity": 3}, {"name": "carrot","type": "vegetable","quantity": 3}]}

        message_json = json.dumps(message)
        messagetwo_json = json.dumps(messagetwo)
        grocery = Grocerystats('fruit')
        grocery.handle_message(message_json)

        self.assertEqual(grocery.handle_message(messagetwo_json), 4.5)


    def test_calculate_average_amount(self):
        message = {"shopper": {"name": "John Smith","gender": "male"},"amount": 47.00,"cart": [{"name": "apple","type": "fruit","quantity": 4}, {"name": "orange","type": "fruit","quantity": 2}]}
        messagetwo = {"shopper": {"name": "John Smith","gender": "male"},"amount": 53.00,"cart": [{"name": "water","type": "beverage","quantity": 3}, {"name": "carrot","type": "vegetable","quantity": 3}]}

        message_json = json.dumps(message)
        messagetwo_json = json.dumps(messagetwo)
        grocery = Grocerystats('fruit')

        grocery.calculate_average_amount(message_json)
        self.assertEqual(grocery.calculate_average_amount(messagetwo_json), 50)

    def test_handle_message_two(self):
        message = {"shopper": {"name": "John Smith","gender": "male"},"amount": 47.00,"cart": [{"name": "apple","type": "fruit","quantity": 4}, {"name": "orange","type": "fruit","quantity": 2}]}
        messagetwo = {"shopper": {"name": "John Smith","gender": "male"},"amount": 53.00,"cart": [{"name": "water","type": "beverage","quantity": 3}, {"name": "carrot","type": "vegetable","quantity": 3}]}

        message_json = json.dumps(message)
        messagetwo_json = json.dumps(messagetwo)
        grocery = Grocerystats(['fruit', 'beverage', 'vegetable'])

        grocery.handle_message_two(message_json)
        self.assertEqual(grocery.handle_message_two(messagetwo_json), {'fruit': 3, 'beverage': 1.5, 'vegetable': 1.5})
