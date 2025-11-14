import json

class Item:
# (by XIE) class to represent an item in the system
    

    
    def __init__(self, name, contact, item_type, item_description="",
                 location='',status=None,lost_or_found=None,item_id=None): 
    #initializes an Item object with provided attributes
        self.name = name
        self.contact = contact #owner's contact information, phone, email, etc.
        self.item_type = item_type #e.g., electronics, clothing, etc.
        self.item_description = item_description
        self.location = location #location where the item was found
        self.status = status #False means unclaimed or unfound(for lost items), True means claimed
        self.lost_or_found = lost_or_found #False=lost;True=found
        self.item_id = item_id #unique identifier for the item


    def __str__(self):
        # this function is to print the details of an item object

        '''String representation of the Item object
        example output:
        Item(ID:1, Name:Phone, Contact:a123456, Type:Electronics, Description:Black iPhone, Status:Unclaimed)'''

        if self.status == False and self.lost_or_found == False:
            status_str = "Unfound"
        elif self.status == False and self.lost_or_found == True:
            status_str = "Unclaimed"
        elif self.status == True and self.lost_or_found == False:
            status_str = "Unfound"
        elif self.status == True and self.lost_or_found == True:
            status_str = "Claimed"

        return (f" "
        f"ID:{self.item_id}\n "
        f"Name:{self.name}\n "
        f"Contact:{self.contact}\n "
        f"Type:{self.item_type}\n "
        f"Description:{self.item_description}\n "
        f"Location:{self.location}\n "
        f"Status:{status_str}"
        )

    def to_dict(self):
        # convert Item object to dictionary; Useful for saving items to json files
        return {
            "item_id": self.item_id,
            "name": self.name,
            "contact": self.contact,
            "item_type": self.item_type,
            "item_description": self.item_description,
            "location": self.location,
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
            location=data.get("location"),
            status=data.get("status", False),
            lost_or_found=data.get("lost_or_found")
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