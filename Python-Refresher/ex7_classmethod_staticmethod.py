# This coding exercise requires you yo complete two method implementation
# 1. The franchise method, which takes in a store as argument. It should return
# a new Store object, with a name equal to the argument + " - franchise"
#
# 2. The store_details method, which also takes in a store as argument. It
# should return a string representing the argument


class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        self.items.append({
            'name': name,
            'price': price
        })

    def stock_price(self):
        total = 0
        for item in self.items:
            total += item['price']
        return total

    @classmethod
    def franchise(cls, store):
        # Return another store, with the same name as the argument's name,
        # plus " - franchise"
        # @classmethod uses keyword cls (meaning class name)
        return cls(store.name + " - franchise")  # new object using cls

    @staticmethod
    def store_details(store):
        # Return a string representing the argument
        # It should be in the format 'NAME, total stock price: TOTAL'

        # another way for string formating call f-strings (Python 3.6+)
        return f'{store.name}, total stock price: {store.stock_price()}'


store = Store('Test')
store2 = Store('Amazon')
store2.add_item('Keyboard', 160)
print(store2.name)
print(store2.stock_price())

# returns new object initialized by class calling it, Store
print(Store.franchise(store))
print(Store.franchise(store2))


print(Store.store_details(store))
print(Store.store_details(store2))
