"""
Unit test

Testing small pieces or features of the app that don't depend
on anything else

"""

from unittest import TestCase
from models.item import ItemModel


class ItemTest(TestCase):
    def test_create_item(self):
        item = ItemModel('Piano', 20.00)

        self.assertEqual('Piano', item.name, "Error in creating an item")
        self.assertEqual(20.00, item.price)


    def test_json(self):
        item = ItemModel('Piano', 20.00)

        expected = {'name': 'Piano', 'price': 20.00}

        self.assertDictEqual(expected, item.json())

