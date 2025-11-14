import json
import hashlib

from models import Item, User

# to stop for viewing
def hold_on():
    print("---Press ENTER to continue---")
    input()

class System:

    # constructor
    def __init__(self,filename="items.json"):
        #Justin
        self.filename = filename # JSON file to store items
        self.max_id = 0
        self.load_items(self.filename) # load existing items from file
        self.count = 0 # count the number of items
    
    # load items from file
    def load_items(self, filename="items.json"):
        #Justin
        if not filename:
            filename = self.filename
        try:
            with open(filename, "r") as f:
                items_data = json.load(f)
                self.max_id = items_data["max_id"] #load max_id
                items_data = items_data["items"]   #load items list
                self.items = [Item.from_dict(item) for item in items_data]

        # if file not found, start with empty list
        except FileNotFoundError:
            self.max_id = 0
            self.items = []
        except json.JSONDecodeError:
            self.max_id = 0
            self.items = []

    def load_users(self, filename="users.json"):
        pass

    # save items to file
    def add_item(self,lost_or_found):
        #Justin

        if lost_or_found == 'lost':
            Bool_LOF = False
        elif lost_or_found == 'found':
            Bool_LOF = True

        # prompt the user to enter item details
        # applicable for both cases
        name = input("Enter item name: ")
        category = input("Enter item type (e.g., electronics, clothing): ")
        description = input("Enter item description " \
        "(press Enter to leave blank): ")
        statues_input = False # default to unclaimed or unfound(for lost items)

        # applicable for found case
        if lost_or_found == 'found':
            contact = input("Enter your contact information: ")
            location = input("Enter location where the item was found: ")
        else:
            contact = "Not applicable"
            location = "Not applicable"

        # item_id = TODO
        # maybe we should also deine [item_id] here?

        item = Item(name = name, 
                    contact = contact, 
                    category = category,
                    description = description, 
                    location = location,
                    lost_or_found = Bool_LOF,
                    status = statues_input,
                    item_id = self.get_new_item_id())
        
        # add the item to the system
        # and save to the json file
        self.items.append(item)
        self.save_items(self.filename)

        # count the number of items
        self.count += 1

        # load items from js file
        self.load_items(self.filename)

    # save items to file
    def save_items(self, filename=None):
        #Justin

        # save current items to json file
        if not filename:
            filename = self.filename
        data={
            "max_id": self.max_id, # save max_id
            "items": [item.to_dict() for item in self.items] #save items by converting to dict
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4) # pretty print json
        # add a success message
        print(f"Items saved to {filename} successfully.")
    
    def save_users(self, filename="users.json"):
        pass

    def id_item(self, item_id):
        #ZHU
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None
    # search items by keyword
    def search_item(self,keyword):
        #ZHU

        '''searching items's relevant imformation'''
        results=[item for item in self.items
                if keyword.lower() == item.name.lower()
                or keyword.lower () == item.location.lower()
                or keyword.lower () == item.description.lower()]
        print("find relative information :",len(results))        
        enumerate(results)
        list(enumerate(results))
        [*enumerate(results,start=1)]
        if results:
            for i , item in enumerate(results):
                print(i,item)
        else:
            print("unmatched item")
        return results

    # delete item by name
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
            

    # list all unclaimed items
    def list_items(self):
        #ZHU

        '''list all unclaimed items'''
        if not self.items: # it is empty
            print("No items in the system.\n")
            hold_on() # stop to view
            return
        for i,item in enumerate(self.items,1):
            if not item.status:
                print(f"NO.{i} Item is:")
                print(item)

        hold_on() # stop to view

    # claim item by name
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
    
    def get_new_item_id(self):
        # (by XIE) generate a new item_id for a new item
        self.max_id+=1
        return self.max_id
    
    def update_item(self,item_id, **kwargs): 
        #XIE

        # allow updating item information based on item_id
        for item in self.items:
            if item.item_id == item_id:
                for key, value in kwargs.items():
                    if hasattr(item, key):
                        setattr(item, key, value)
                self.save_items() 
                print(f"Item {item_id} updated successfully.")
                return True
        print(f"Item {item_id} not found.")
        return False

    def hash_password(self, password):
        # (by XIE) hash the password using SHA-256
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register(self):
        # (by XIE) register a new user
        print("===== Register interface =====")

        while True: #username input loop
            username = input("Please enter your username (at least 6 characters, q to quit): ").strip()
            if username.lower() == 'q':
                print("Registration cancelled.")
                return
            if not username:
                print("Username cannot be empty.")
                continue
            if len(username) < 6:
                print("Username must be at least 6 characters long.")
                continue
            if any(u.username == username for u in self.users):
                print("Username already exists. Please try another one.")
                continue
            break

        while True: #password input loop
            password = input("Please enter your password (at least 6 characters, q to quit): ").strip()
            if password.lower() == 'q':
                print("Registration cancelled.")
                return
            if not password:
                print("Password cannot be empty.")
                continue
            if len(password) < 6:
                print("Password must be at least 6 characters long.")
                continue
            break
        password = self.hash_password(password) # hash the password before storing

        while True: #role input loop
            role = input("Please enter your role (admin/owner/finder, q to quit): ").strip().lower()
            if role == 'q':
                print("Registration cancelled.")
                return
            if role not in ['admin', 'owner', 'finder']:
                print("Invalid role. Please enter 'admin', 'owner', or 'finder'.")
                continue
            if role == 'admin':
                admin_code = input("Please enter the admin registration code: ").strip()
                if admin_code != "COMP1080": # example admin code
                    print("Invalid admin registration code.")
                    continue
            break
        contact = input("Please enter your contact information (q to quit): ").strip()
        if contact.lower() == 'q':
            print("Registration cancelled.")
            return
        email = input("Please enter your email address (q to quit): ").strip()
        if email.lower() == 'q':
            print("Registration cancelled.")
            return
        
        new_user = User(username, password, role, contact, email)
        self.users.append(new_user)
        self.save_users()
        print("User registered successfully!")
        print(new_user)
        


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

    # main menu
    def main_menu(self):
        #LUO 
        # ---Charlotte also did one---

        while True:
            print("===== Lost and Found System =====")
            print("1. I Lost")
            print("2. I Found")
            print("3. Administrator")
            print("0. Exit")
            choice=input("*Please select an option (0-3): ")  # Main menu selection
            print() # New line for better readability
            if choice == '1':
                self.owner_menu()
            elif choice == '2':
                self.finder_menu()
            elif choice == '3':
                self.admin_menu()
            elif choice == '0':
                self.load_items(self.filename) # make sure json up-to-date
                print("Thank you for using the Lost and Found System! Goodbye!")
                break
            else:
                print("Invalid choice, please try again!") 

    # owner menu
    def owner_menu(self): # lost
        #Charlotte
        # ---LUO also did one---

        while True:
            print("\n===== Owner Menu =====")
            print("1. Search Claimable Items (by keyword)")
            print("2. View All Claimable Items")
            print("3. The item is not in the list?")
            print("0. Return to Main Menu")
            choice = input("*Please select an option [0-3]: ")
            
            if choice == '1':
                print() # New line for better readability
                keyword = input("Enter search keyword (item name/description): ")
                results = self.search_item(keyword)
                if results:
                    for item in results:
                        print(f"ID: {item.item_id} | Name: {item.name}")
                        print(f"Description: {item.description} | Location: {item.location}")
                else:
                    print("No matching items found.")
                hold_on() # stop to view
            
            elif choice == '2':
                print() # New line for better readability
                self.list_items()
            elif choice == '0':
                print() # New line for better readability
                break # exit to main page
            elif choice == '3':
                self.declare_lost()
            else:
                print("Invalid input, please try again.")

    # in case that the item is to be found
    def declare_lost(self): 
        #Justin

        print("Please declare your lost item details:")
        self.add_item(lost_or_found='lost')

    # finder menu
    def finder_menu(self):
        #LUO

        while True:
            print("\n===== Finder Menu =====")
            print("1. Search Claimable Items (by keyword)")
            print("2. View All Claimable Items")
            print("3. Submit Found Item")
            print("0. Return to Main Menu")
            choice=input("*Please select an option (0-3): ")  # User function selection
            if choice == '1':  # Search
                keyword=input("Enter item keyword: ")
                results=self.search_item(keyword)
                if results:
                    for item in results:
                        print(f"Item Name: {item.name}, Description: {item.description}, "
                              f"Found Location: {item.location}")
                else:
                        print("No matching items found.")
                hold_on() # viewing
            elif choice == '2':  # View
                self.list_items()
            elif choice == '3':  # Submit
                self.add_item(lost_or_found='found')
                print("Found item submitted successfully!")
            elif choice == '0':
                break
                print("Back to main menu")
            else:
                print("Invalid choice, please try again!")
    
    # admin menu
    def admin_menu(self):
        #LUO

        while True:
            print("\n===== Administrator Menu =====")
            print("1. Delete Item")
            print("2. View Items (Claimed/Unclaimed)")
            print("0. Return to Main Menu")
            choice=input("*Please select an option [0-3]: ")  # Admin input
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
    system.update_item(item.item_id, category="Apple iphone", description="white iphone")
    print(item)
    result = system.update_item(2, description="test")
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
