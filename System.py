import json
from Item import Item



class System:
    def __init__(self,filename="items.json"):
        #Justin
        self.filename = filename
        self.items = []  
        self.max_id = 0
        self.load_items()
    
    def load_items(self):
        pass
    def add_item(self, item):
        #Justin
        self.items.append(item)
    def save_items(self, filename):
        #Justin
        pass
    def search_items(self, keyword):
        #ZHU
        pass
   
    def delete_item(self, item_name):
        #ZHU
        pass
    
    def list_items(self):
        #ZHU
        pass
    def claim_item(self, item_name, owner_contact):
        #Charlotte
        pass

    def get_new_item_id(self):
        # (by XIE) generate a new item_id for a new item
        self.max_id+=1
        self.save_items(self.filename)  #change save_items(...) if parameters are changed
        return self.max_id
    
    
    def update_item(self,item_id, **kwargs): 
        # (by XIE) allow updating item information based on item_id
        for item in self.items:
            if item.item_id == item_id:
                for key, value in kwargs.items():
                    if hasattr(item, key):
                        setattr(item, key, value)
                self.save_items(self.filename)  #change save_items(...) if parameters are changed
                print(f"Item {item_id} updated successfully.")
                return True
        print(f"Item {item_id} not found.")
        return False

    def login(self):
        #Charlotte
        pass
    def main_menu(self):
        #Charlotte
        pass    
    def owner_menu(self, owner_contact):
        #LUO
        pass
    def finder_menu(self):
        #LUO
        pass
    
    def admin_menu(self):
        #LUO
        pass

if __name__ == "__main__":
    system = System()
    system.main_menu()


"""
# Test cases for update_item method
if __name__ == "__main__":
    system = System()

    item = Item("phone", "a123456", "Electronics", "Silver iphone")
    system.add_item(item)
    print(item)
    system.update_item(item.item_id, item_type="Apple iphone", item_description="white iphone")
    print(item)
    result = system.update_item(2, item_description="test")
    print("Return:", result)
"""