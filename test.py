from grocerystats import Grocerystats
import unittest

class GrocerystatsTest(unittest.TestCase):

    # test class creation
    def test_create_grocery(self):
        grocery = Grocerystats('vegetable')
        self.assertEqual(grocery.type, 'vegetable')
        self.assertEqual(grocery.total_sales, 0)
        self.assertEqual(grocery.total_quantity, 0)

