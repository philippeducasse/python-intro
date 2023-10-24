class ShoppingList(object):
    def __init__(self, list_name):
        self.list_name = list_name
        self.shopping_list = []

        def add_item(self, item):
            added_item = str(input("Enter an item: "))
            if not added_item in self.shopping_list:
                self.shopping_list.append(added_item)
                return self.shopping_list

        def remove_item(self, item):
            self.item = str(input("Enter an item: "))
            self.shopping_list.remove(item)
            return self.shopping_list

        def view_list(self):
            print(self.shopping_list)


pet_store_list = ShoppingList("Pet Store Shopping List")

pet_store_list.add_item()
