import json

class Item:
# (by XIE) class to represent an item in the system
    
    count=1 #for unique item IDs
    
    def __init__(self, name, contact, item_type, item_description="", status=False,item_id=None): 
    #initializes an Item object with provided attributes
        self.name = name
        self.contact = contact #owner's contact information, phone, email, etc.
        self.item_type = item_type #e.g., electronics, clothing, etc.
        self.item_description = item_description
        self.status = status #False means unclaimed, True means claimed
        if item_id is None:
            self.item_id = Item.count
            Item.count += 1
        else:
            self.item_id = item_id
        

  
    def __str__(self):

        '''String representation of the Item object
        example output:
        Item(ID:1, Name:Phone, Contact:a123456, Type:Electronics, Description:Black iPhone, Status:Unclaimed)'''

        status_str = "Claimed" if self.status else "Unclaimed"
        return (f"Item("
        f"ID:{self.item_id}, "
        f"Name:{self.name}, "
        f"Contact:{self.contact}, "
        f"Type:{self.item_type}, "
        f"Description:{self.item_description}, "
        f"Status:{status_str}"
        f")"
        )

    def to_dict(self):
        # convert Item object to dictionary; Useful for saving items to json files
        return {
            "item_id": self.item_id,
            "name": self.name,
            "contact": self.contact,
            "item_type": self.item_type,
            "item_description": self.item_description,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        # create Item object from dictionary; Useful for loading items from json files
        return Item(
            item_id=data.get("item_id"),
            name=data.get("name"),
            contact=data.get("contact"),
            item_type=data.get("item_type"),
            item_description=data.get("item_description"),
            status=data.get("status", False)
        )


'''
# Test cases for Item class
if __name__ == "__main__":
    item1 = Item("iphone", "a123456", "Electronics", "black iPhone") # Create an item instance
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