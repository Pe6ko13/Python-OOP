class Shop:
    def __init__(self, name, items):
        self.name = name
        self.items = items
        self.count = 0

    def get_items_count(self):
        for _ in self.items:
            self.count += 1
        return self.count


shop = Shop("My Shop", ["Apples", "Bananas", "Cucumbers"])
print(shop.get_items_count())
