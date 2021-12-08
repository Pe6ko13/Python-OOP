from project.pet_shop import PetShop
from unittest import TestCase, main


class TestPetShop(TestCase):
    def setUp(self) -> None:
        self.shop = PetShop('P')

    def test_init(self):
        self.assertEqual('P', self.shop.name)
        self.assertEqual({}, self.shop.food)
        self.assertEqual([], self.shop.pets)

    def test_add_food_if_quantity_less_than_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.shop.add_food('n', -5)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food_if_quantity_zero(self):
        with self.assertRaises(ValueError) as ex:
            self.shop.add_food('n', 0)
        self.assertEqual('Quantity cannot be equal to or less than 0', str(ex.exception))

    def test_add_food(self):
        res = self.shop.add_food('n', 2)
        self.assertEqual({'n': 2}, self.shop.food)
        self.assertEqual(res, "Successfully added 2.00 grams of n.")

    def test_add_pet_already_added(self):
        self.shop.add_pet('puh')
        with self.assertRaises(Exception) as ex:
            self.shop.add_pet('puh')
        self.assertEqual("Cannot add a pet with the same name", str(ex.exception))

    def test_add_pet(self):
        res = self.shop.add_pet('po')
        self.assertEqual(res, "Successfully added po.")
        self.assertEqual(['po'], self.shop.pets)

    def test_feed_pet_not_present(self):
        with self.assertRaises(Exception) as ex:
            self.shop.feed_pet('ror', 'po')
        self.assertEqual('Please insert a valid pet name', str(ex.exception))

    def test_feed_pet_food_not_present(self):
        self.shop.add_pet('po')
        res = self.shop.feed_pet('ror', 'po')
        self.assertEqual(res, 'You do not have ror')

    def test_feed_pet_if_food_less_than_100(self):
        self.shop.add_pet('po')
        self.shop.add_food('n', 2)
        res = self.shop.feed_pet('n', 'po')
        self.assertEqual(res, "Adding food...")
        self.assertEqual({'n': 1002}, self.shop.food)

    def test_feed_pet(self):
        self.shop.add_pet('po')
        self.shop.add_food('n', 200)
        res = self.shop.feed_pet('n', 'po')
        self.assertEqual(res, "po was successfully fed")
        self.assertEqual({'n': 100}, self.shop.food)

    def test_repr(self):
        self.shop.add_pet('po')
        self.shop.add_food('n', 200)
        massage = 'Shop P:\n' \
               'Pets: po'
        res = self.shop.__repr__()
        self.assertEqual(res, massage)


if __name__ == '__main__':
    main()
