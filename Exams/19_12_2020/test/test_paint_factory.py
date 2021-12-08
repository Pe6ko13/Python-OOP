from unittest import TestCase, main

from project.factory.paint_factory import PaintFactory


class TestPaintFactory(TestCase):
    def setUp(self) -> None:
        self.pf = PaintFactory('Tes', 100)

    def test_init(self):
        self.assertEqual('Tes', self.pf.name)
        self.assertEqual(100, self.pf.capacity)
        self.assertEqual({}, self.pf.ingredients)
        self.assertEqual(["white", "yellow", "blue", "green", "red"], self.pf.valid_ingredients)

    def test_add_ingredient_invalid_product_type(self):
        with self.assertRaises(TypeError) as ex:
            self.pf.add_ingredient('black', 2)
        self.assertEqual("Ingredient of type black not allowed in PaintFactory", str(ex.exception))

    def test_add_ingredient_invalid_quantity(self):
        with self.assertRaises(ValueError) as ex:
            self.pf.add_ingredient('white', 101)
        self.assertEqual("Not enough space in factory", str(ex.exception))

    def test_add_ingredient_valid_product(self):
        self.assertEqual({}, self.pf.ingredients)
        self.pf.add_ingredient('white', 2)
        self.assertEqual({'white': 2}, self.pf.ingredients)

    def test_add_ingredient_already_in_dic(self):
        self.assertEqual({}, self.pf.ingredients)
        self.pf.add_ingredient('white', 2)
        self.assertEqual({'white': 2}, self.pf.ingredients)
        self.pf.add_ingredient('white', 2)
        self.assertEqual({'white': 4}, self.pf.ingredients)

    def test_remove_ingredient_not_in_dic(self):
        with self.assertRaises(KeyError) as ex:
            self.pf.remove_ingredient('black', 1)
        self.assertEqual("'No such ingredient in the factory'", str(ex.exception))

    def test_remove_ingredient_cannot_be_negative(self):
        self.pf.add_ingredient('white', 2)
        with self.assertRaises(ValueError) as ex:
            self.pf.remove_ingredient('white', 3)
        self.assertEqual("Ingredients quantity cannot be less than zero", str(ex.exception))

    def test_remove_ingredient(self):
        self.pf.add_ingredient('white', 2)
        self.pf.remove_ingredient('white', 1)
        self.assertEqual({'white': 1}, self.pf.ingredients)

    def test_products_property(self):
        self.pf.add_ingredient('white', 2)
        self.assertEqual({'white': 2}, self.pf.products)


if __name__ == '__main__':
    main()
