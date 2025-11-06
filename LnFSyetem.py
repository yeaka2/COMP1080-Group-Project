import json
from item import Item

class LnFSyetem:
    def __init__(self,filename="items.json"):
        #Justin
        self.filename = filename
        self.items = []  
    
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
    def login(self):
        #Charlotte
        pass
    def owner_menu(self, owner_contact):
        #Charlotte
        pass
    def finder_menu(self):
        #LUO
        pass
    def main_menu(self):
        #LUO
        pass
    def admin_menu(self):
        #LUO
        pass


    