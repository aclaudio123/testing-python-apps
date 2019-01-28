from models.item import ItemModel
from tests.base_test import BaseTest


class ItemTest(BaseTest):
    def test_crud(self):
        with self.app_context:
            item = ItemModel('Piano', 20.00)

            # assert item does not exit in db
            self.assertIsNone(ItemModel.find_by_name('Piano'),
                              f'Error: found item {item.name} in db, but expected not to.')

            item.save_to_db()

            # assert item does exit
            self.assertIsNotNone(ItemModel.find_by_name('Piano'),
                                 f'Error: did not find item {item.name} in db, but expected to.')

            item.delete_from_db()

            self.assertIsNone(ItemModel.find_by_name('Piano'))
