import json
from Item import Item

class System:
    def __init__(self,filename="items.json"):
        #Justin
        self.filename = filename # JSON file to store items
        self.load_items(self.filename) # load existing items from file
        self.count = 0 # count the number of items
    
    def load_items(self, filename=None):
        #Justin
        if not filename:
            filename = self.filename
        try:
            with open(filename, "r") as f:
                items_data = json.load(f)
                self.items = [Item.from_dict(item) for item in items_data]

        # if file not found, start with empty list
        except FileNotFoundError:
            self.items = []
        except json.JSONDecodeError:
            self.items = []

    def add_item(self, item):
        #Justin

        # prompt the user to enter item details
        name = input("Enter item name: ")
        contact = input("Enter owner contact information: ")
        item_type = input("Enter item type (e.g., electronics, clothing): ")
        item_description = input("Enter item description: \n" \
        "(press Enter to leave blank): ")
        statues_input = input("Is the item claimed or unclaimed (yes/no): ")
        item = Item(name, contact, item_type, item_description, statues_input == "yes")
        
        # add the item to the system
        # and save to the json file
        self.items.append(item)
        self.save_items(self.filename)

        # count the number of items
        self.count += 1

    def save_items(self, filename=None):
        #Justin

        # save current items to json file
        if not filename:
            filename = self.filename
        with open(filename, "w") as f:
            json.dump([item.__dict__ for item in self.items], f)
        # add a success message
        print(f"Items saved to {filename} successfully.")

    def search_item(self,keyword):
        #ZHU

        '''searching items's relevant imformation'''
        results=[item for item in self.items
                if keyword.lower() == item.name.lower()
                or keyword.lower () == item.location.lower()
                or keyword.lower () == item.location.lower()]
        print("find relative information :",len(results))        
        enumerate(results)
        list(enumerate(results))
        [*enumerate(results,start=1)]
        if results:
            for i , item in enumerate(results):
                print(i,item)
        else:
            print(" unmatched item")
        return results

    def delete_item(self,item_name):
        #ZHU

        '''delete finding items '''
        original_items_len=len(self.items)
        self.items=[item for item in self.items 
                    if item.name !=item_name]
        for  j , item in enumerate(self.items,1):
            if item.name==item_name:
                del self.items[j]
                print('The item has been deleted')
                return
        if len(self.items) < original_items_len:
            self.save_items()
            print('The item has been saved')
        else:
            print("The item has not been found")

    def list_items(self):
        #ZHU

        '''list all unclaimed items'''
        for i , item in enumerate(self.items,1):
            if not item.is_claimed:
                print(f"{i},the name is {item.name}")
                print(f" the location is{item.location} ")
                print(f" the location is{item.location} ")

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

    def update_item(self,item_id, **kwargs): 
        #XIE

        # allow updating item information based on item_id
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

    def main_menu(self):
        #LUO 
        # ---Charlotte also did one---

        while True:
            print("\n===== Lost and Found System =====")
            print("1. I Found / Lost Something! (finder&owner)")
            print("2. I'm an Administrator! (admin)")
            print("0. Exit System")
            choice=input("Please select an option (0-2): ")  # Main menu selection
            if choice == '1':
                self.finder_menu()
            elif choice == '2':
                self.admin_menu()
            elif choice == '0':
                print("Thank you for using the Lost and Found System! Goodbye!")
                break
            else:
                print("Invalid choice, please try again!")    

    def owner_menu(self, owner_contact):
        #Charlotte
        # ---LUO also did one---

        while True:
            print("\n===== Owner Menu =====")
            print("1. Search Claimable Items (by keyword)")
            print("2. View All Claimable Items")
            print("0. Return to Main Menu")
            
            choice = input("Please select an option [0-3]: ")
            
            if choice == '1':
                keyword = input("Enter search keyword (item name/description): ")
                results = self.search_items(keyword)
                if results:
                    for item in results:
                        print(f"ID: {item.item_id} | Name: {item.name} | Description: {item.description} | Location: {item.location}")
                else:
                    print("No matching items found.")
            
            elif choice == '2':
                self.list_items()
            elif choice == '0':
                break
            
            else:
                print("Invalid input, please try again.")

    def finder_menu(self):
        #LUO

        while True:
            print("\n===== Finder Menu =====")
            print("1. Search Claimable Items (by keyword)")
            print("2. View All Claimable Items")
            print("3. Submit Found Item")
            print("0. Return to Main Menu")
            choice=input("Please select an option (0-3): ")  # User function selection
            if choice == '1':  # Search
                keyword=input("Enter item keyword: ")
                results=self.search_item(keyword)
                if results:
                    for item in results:
                        print(f"Item Name: {item.name}, Description: {item.description}, Found Location: {item.destination}")
                else:
                        print("No matching items found.")
            elif choice == '2':  # View
                self.list_items()
            elif choice == '3':  # Submit
                name=input("Enter found item name: ")
                description=input("Enter item description: ")
                location=input("Enter found location: ")
                new_item=Item(name=name,description=description,destination=destination)
                self.add_item(new_item)
                print("Found item submitted successfully!")
            elif choice == '0':
                break
                print("Back to main menu")
            else:
                print("Invalid choice, please try again!")
    
    def admin_menu(self):
        #LUO

        while True:
            print("\n===== Administrator Menu =====")
            print("1. Delete Item")
            print("2. View Items (Claimed/Unclaimed)")
            print("0. Return to Main Menu")
            choice=input("Please select an option [0-3]: ")  # Admin input
            if choice == '1':  # Delete item
                item_id=input("Enter item ID to delete: ")
                # Note: item_id is necessary, can be assigned using index
                if self.delete_item(item_id):
                    print("Item deleted successfully.")
                else:
                    print("Item not found.")
            elif choice == '2':
                # Note: For better display, originally planned to show claimed/unclaimed counts separately,
                # but simplified to list all items since there's no item_status in the previous implementation
                self.list_items()
            elif choice == '0':
                break
                print("Returning to main menu")
            else:
                print("Invalid choice, please try again!")

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
"""
Contributer denote:
XIE: XIE Zhiyuan
Justin: LIAO Junming
ZHU: ZHU Jinze
Charlotte: LUO wenqi
LUO: LUO Zhenyu
"""