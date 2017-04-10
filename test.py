from grocerystats import Grocerystats
import unittest

class GrocerystatsTest(unittest.TestCase):

    # test class creation
    def test_create_grocery(self):
        grocery = Grocerystats('vegetable')
        self.assertEqual(grocery.type, 'vegetable')
        self.assertEqual(grocery.total_sales, 0)
        self.assertEqual(grocery.total_quantity, 0)

    def test_add_sale(self):
        grocery = Grocerystats('fruit')
        grocery.add_sale()
        grocery.add_sale()

        self.assertEqual(grocery.total_sales, 2)

