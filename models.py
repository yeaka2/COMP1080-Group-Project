import json

class User:
# (by XIE) class to represent a user in the system
    def __init__(self, username, password, role, contact='', email=''):
        self.username = username
        self.password = password
        self.role = role #e.g., admin, owner, finder
        self.contact = contact
        self.email = email

    def __str__(self):
        # this function is to print the details of a user object
        return (f"Username: {self.username}\n"
                f"Role: {self.role}\n"
                f"Contact: {self.contact}\n"
                f"Email: {self.email}\n")
    
    def to_dict(self):
        # convert User object to dictionary; Useful for saving users to json files
        return {
            "username": self.username,
            "password": self.password,
            "role": self.role,
            "contact": self.contact,
            "email": self.email
        }
    
    @staticmethod
    def from_dict(data):
        # create User object from dictionary; Useful for loading users from json files
        return User(
            username=data['username'], # mandatory fields
            password=data['password'], # mandatory fields
            role=data['role'], # mandatory fields
            contact=data.get('contact',''), # optional fields
            email=data.get('email','') # optional fields
        )
    
class Item:
# (by XIE) class to represent an item in the system
    

    
    def __init__(self, name, contact, category, description="",
                 location='',status=None,lost_or_found=None,item_id=None): 
    #initializes an Item object with provided attributes
        self.name = name
        self.contact = contact #owner's contact information, phone, email, etc.
        self.category = category #e.g., electronics, clothing, etc.
        self.description = description
        self.location = location #location where the item was found
        self.status = status #False means unclaimed or unfound(for lost items), True means claimed
        self.lost_or_found = lost_or_found #False=lost;True=found
        self.item_id = item_id #unique identifier for the item


    def __str__(self):
        # this function is to print the details of an item object

        '''String representation of the Item object
        example output:
        Item(ID:1, Name:Phone, Contact:a123456, category:Electronics, Description:Black iPhone, Status:Unclaimed)'''

        if self.status == False and self.lost_or_found == False:
            status_str = "Unfound"
        elif self.status == False and self.lost_or_found == True:
            status_str = "Unclaimed"
        elif self.status == True and self.lost_or_found == False:
            status_str = "Unfound"
        elif self.status == True and self.lost_or_found == True:
            status_str = "Claimed"
        else:
            status_str = "Unknown"

        return (f" "
        f"ID:{self.item_id}\n "
        f"Name:{self.name}\n "
        f"Contact:{self.contact}\n "
        f"Category:{self.category}\n "
        f"Description:{self.description}\n "
        f"Location:{self.location}\n "
        f"Status:{status_str}"
        )

    def to_dict(self):
        # convert Item object to dictionary; Useful for saving items to json files
        return {
            "item_id": self.item_id,
            "name": self.name,
            "contact": self.contact,
            "Category": self.category,
            "Description": self.description,
            "Location": self.location,
            "Status": self.status,
            "Lost_or_found": self.lost_or_found
        }

    @staticmethod
    def from_dict(data):
        # create Item object from dictionary; Useful for loading items from json files
        return Item(
            item_id=data.get("item_id"),
            name=data.get("name"),
            contact=data.get("contact"),
            category=data.get("Category"),
            description=data.get("Description"),
            location=data.get("Location"),
            status=data.get("Status", False),
            lost_or_found=data.get("Lost_or_found")
        )


'''
# Test cases for Item class
if __name__ == "__main__":
    item1 = Item("iphone", "a123456", "Electronics", "black iPhone","IOH") # Create an item instance
    print(item1)  #test __str__

    # to dict and from dict test
    d = item1.to_dict()
    print("Dict:", d)
    item2 = Item.from_dict(d)
    print("From dict:", item2)

    # test status display
    item1.status = True
    print("Claimed:", item1)
    item1.status = False
    print("Claimed:", item1)
'''
