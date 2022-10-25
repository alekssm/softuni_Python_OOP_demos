class Shop:
    _small_shop_capacity = 10

    def __init__(self, name: str, type: str, capacity: int):
        self.name = name
        self.type = type
        self.capacity = capacity
        self.item_count = 0
        self.items = {}

    @classmethod
    def small_shop(cls, name: str, type: str):
        return Shop(name, type, cls._small_shop_capacity)

    def _not_enough_capacity(self):
        return self.item_count >= self.capacity

    def _can_not_remove_item(self, item_name, quantity):
        if item_name not in self.items:
            return True
        if self.items[item_name] < quantity:
            return True
        return False

    def add_item(self, item_name: str):
        if self._not_enough_capacity():
            return "Not enough capacity in the shop"
        if item_name not in self.items:
            self.items[item_name] = 0
        self.items[item_name] += 1
        self.item_count += 1
        return f"{item_name} added to the shop"

    def remove_item(self, item_name:str, amount:int):
        if self._can_not_remove_item(item_name, amount):
            return f"Cannot remove {amount} {item_name}"
        self.items[item_name] -= amount
        self.item_count -= amount
        return f"{amount} {item_name} removed from the shop"

    def __repr__(self):
        return f"{self.name} of type {self.type} with capacity {self.capacity}"


fresh_shop = Shop("Fresh Shop", "Fruit and Veg", 50)
small_shop = Shop.small_shop("Fashion Boutique", "Clothes")
print(fresh_shop)
print(small_shop)

print(fresh_shop.add_item("Bananas"))
print(fresh_shop.remove_item("Tomatoes", 2))

print(small_shop.add_item("Jeans"))
print(small_shop.add_item("Jeans"))
print(small_shop.remove_item("Jeans", 2))
