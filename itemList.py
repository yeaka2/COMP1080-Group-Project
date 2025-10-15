from lostItem import lostItem

class itemList:
    # Using add_item(), delete_item(), search_item(), 
    # upload_item(), search_item(), etc. 
    # to implement the main functional modules
    def __init__(self):
        self.items = []
        self.size = 0
        # we often have id = size + 1
        # but there is still special cases
        # we have set to tackle them although it will not happen normally

    def add_item(self, item): # Add a lostItem object
        self.items.append(item)
        self.size += 1

    def upload_item(self, id = None):
        if id is None:
            id = self.size + 1
        description = input("Enter item description: ")
        location_found = input("Enter location found: ")
        date_found = input("Enter date found (YYYY-MM-DD): ")
        new_item = lostItem(item_id=id, description=description, \
                            location_found=location_found, date_found=date_found)
        self.add_item(new_item)

    def delete_item(self, item_id): # Delete item by item_id
        self.items.remove(self.search_item(item_id))
        self.size -= 1

    def search_item(self, item_id):
        for item in self.items:
            if item.item_id == item_id:
                return item
        return None

    def list_all_items(self):
        for item in self.items:
            print(item)