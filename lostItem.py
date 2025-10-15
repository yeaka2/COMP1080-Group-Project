class lostItem:
    def __init__(self, item_id = 0, description = None, location_found = "Unknown", date_found = "Unknown"):
        self.item_id = int(item_id)
        self.description = description
        self.location_found = location_found
        self.date_found = date_found

    def __repr__(self):
        return (f"lostItem(item_id={self.item_id}, description='{self.description}', "
                f"location_found='{self.location_found}', date_found='{self.date_found}')")