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
        """Claim your lost item (operation by the owner)"""
        for item in self.items:
            if item.item_name == item_name:
                # If the item has already been claimed
                if hasattr(item, "claimed") and item.claimed:
                    print(" The item has been claimed.")
                    return False
                # Modify item status
                item.claimed = True
                item.owner_contact = owner_contact
                self.save_items(self.filename)
                print(f" Item '{item_name}' has been claimed by {owner_contact}.")
                return True
        print(f" No item named '{item_name}' was found.")
        return False

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
        """Login portal"""
        print("===== Login interface =====")
        username = input("Please enter your username： admin / owner / finder：").strip()
        if username == "admin":
            self.admin_menu()
        elif username == "owner":
            contact = input("Please fill in your contact information (mobile phone number or email address):")
            self.owner_menu(contact)
        elif username == "finder":
            self.finder_menu()
        else:
            print("Invalid username, please re-enter.")

        pass
    def main_menu(self):
        #Charlotte
        """Main Menu"""
        while True:
            print("\n===== Lost and Found System =====")
            print("1. Log in")
            print("2. Browse items")
            print("3. Search items")
            print("0. Log out")
            choice = int(input("Please enter options:"))

            if choice == "1":
                self.login()
            elif choice == "2":
                self.list_items()
            elif choice == "3":
                keyword = input("Please enter keywords:")
                self.search_items(keyword)
            elif choice == "0":
                print(" bye!")
                break
            else:
                print(" Invalid option, please try again.")
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
