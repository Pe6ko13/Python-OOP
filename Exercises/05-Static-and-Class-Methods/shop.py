class Shop:

    def __init__(self, name, type, capacity):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.items = {}
        # {'item_name': quantity}

    @classmethod
    def small_shop(cls, name: str, s_type: str):
        return cls(name, s_type, 10)

    def add_item(self, item_name: str):
        if 0 < self.capacity:
            if item_name not in self.items:
                self.items[item_name] = 0
            self.items[item_name] += 1
            self.capacity -= 1
            return f"{item_name} added to the shop"
        return "Not enough capacity in the shop"

    def remove_item(self, item_name: str, amount: int):
        if item_name in self.items:
            if self.items[item_name] >= amount:
                self.items[item_name] -= amount
                self.capacity += amount
                return f"{amount} {item_name} removed from the shop"
            return f"Cannot remove {amount} {item_name}"
        return f"Cannot remove {amount} {item_name}"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


from unittest import TestCase, main


class TestShop(TestCase):
    def setUp(self) -> None:
        self.shop = Shop('P', 'FR', 10)

    def test_init(self):
        self.assertEqual('P', self.shop.name)
        self.assertEqual('FR', self.shop.type)
        self.assertEqual(10, self.shop.capacity)
        self.assertEqual({}, self.shop.items)

    def test_add_item(self):
        self.shop.capacity = -1
        res = self.shop.add_item('ban')
        self.assertEqual("Not enough capacity in the shop", res)

    def test_add_item_if_no_item(self):
        res = self.shop.add_item('ban')
        self.assertEqual({'ban': 1}, self.shop.items)
        self.assertEqual(res, f"ban added to the shop")

    def test_add_item_if_item(self):
        self.shop.add_item('ban')
        res = self.shop.add_item('ban')
        self.assertEqual({'ban': 2}, self.shop.items)
        self.assertEqual(res, f"ban added to the shop")

    def test_remove_item(self):
        self.shop.add_item('ban')
        self.shop.add_item('ban')
        self.shop.remove_item('ban', 1)
        self.assertEqual({'ban': 1}, self.shop.items)

    def test_remove_item_if_amount_bigger(self):
        self.shop.add_item('ban')
        res = self.shop.remove_item('ban', 5)
        self.assertEqual(res, "Cannot remove 5 ban")

    def test_remove_item_if_is_not_there(self):
        res = self.shop.remove_item('ban', 5)
        self.assertEqual(res, "Cannot remove 5 ban")


if __name__ == '__main__':
    main()
