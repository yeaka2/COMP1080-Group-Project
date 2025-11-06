import json

class Item:
    def __init__(self, name, contact, item_type, item_description="", found=False):
        self.name = name
        self.contact = contact
        self.item_type = item_type
        self.found = found
        self.item_description = item_description

    def to_dict(self):
        return {
            "name": self.name,
            "contact": self.contact,
            "item_type": self.item_type,
            "item_description": self.item_description,
            "found": self.found
        }

    @staticmethod
    def from_dict(data):
        return Item(
            name=data.get("name"),
            contact=data.get("contact"),
            item_type=data.get("item_type"),
            item_description=data.get("item_description"),
            found=data.get("found", False)
        )
