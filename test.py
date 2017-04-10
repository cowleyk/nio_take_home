from grocerystats import Grocerystats
import unittest

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
        grocery.add_quantity()
        grocery.add_quantity()

        self.assertEqual(grocery.total_quantity, 2)

    # not testing message string to json conversion, assuming json.loads() works

    # test 'cart' isolation
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


