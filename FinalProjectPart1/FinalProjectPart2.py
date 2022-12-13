# Antwon Limbrick 1972657
# Final Project Part 2


import csv
from datetime import datetime

class OutputInventory:                                           # Class for methods used to create output inventory files from provided input
    def __init__(self, item_list):                               # Files created under the output_files directory.
        self.item_list = item_list                               # The list of all items to create new files
    
    def full(self):                                               # Creates a csv output file for the entire inventory.
        with open('FullInventory.csv', 'w') as file:                 # The items are sorted alphabetically by manufacturer
            items = self.item_list
            def get_manufacturer(x):                                 # The get_manufacturer is used get order of keys to write to file based on manufacturer
                return items[x]['manufacturer']
            keys = sorted(items.keys(), key=get_manufacturer)
            for item in keys:
                id = item
                man_name = items[item]['manufacturer']                         # Opens an new file to write list of items into FullInventory.csv file
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                file.write('{},{},{},{},{},{}\n'.format(id,man_name,item_type,price,service_date,damaged))   
                
    def by_type(self):                                                    # Creates a csv output file for items based by type
        items = self.item_list                                              # Each type gets its own file. Type is reflected in the name of file
        types = []
        keys = sorted(items.keys())
        for item in items:
            item_type = items[item]['item_type']
            if item_type not in types:
                types.append(item_type)
        for type in types:
            file_name = type.capitalize() + 'Inventory.csv'
            with open(file_name, 'w') as file:
                for item in keys:
                    id = item
                    man_name = items[item]['manufacturer']                # Items are then sorted by item ID while each row contains the data
                    price = items[item]['price']
                    service_date = items[item]['service_date']
                    damaged = items[item]['damaged']
                    item_type = items[item]['item_type']
                    if type == item_type:
                        file.write('{},{},{},{},{}\n'.format(id, man_name, price, service_date, damaged))
    
    def past_service(self):                                     # past_service creates a csv output file for items which are past the service date (expiration is date executed)
        items = self.item_list
        def get_servicedate(x):                                 # The get_servicedate is used get order of keys to write to file based on service date
            return items[x]['service_date']
        keys = sorted(items.keys(), key=get_servicedate)
        with open('PastServiceDateInventory.csv', 'w') as file:
            for item in keys:                                      # The items are sorted from oldest to most recent
                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                today = datetime.now().date()
                service_expiration = datetime.strptime(service_date, "%m/%d/%Y").date()   # Opens an new file to write list of items into PastServiceDateInventory.csv file
                expired = service_expiration < today
                if expired:
                    file.write('{},{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date, damaged))
    
    
    def damaged(self):
        items = self.item_list
        def get_serviceprice(x):                                 # The get_serviceprice is used get order of keys to write to file based on price
            return items[x]['price']
        keys = sorted(items.keys(), key=get_serviceprice)
        with open('DamagedInventory.csv', 'w') as file:                     # Creates a csv output file for all items that are damaged.
            for item in keys:
                id = item
                man_name = items[item]['manufacturer']
                item_type = items[item]['item_type']
                price = items[item]['price']                                 # Opens an new file to write list of items into DamagedInventory.csv file
                service_date = items[item]['service_date']
                damaged = items[item]['damaged']
                if damaged:
                    file.write('{},{},{},{},{}\n'.format(id, man_name, item_type, price, service_date))
    
    
if __name__ == '__main__':
    items = {}
    files = ['ManufacturerList.csv', 'PriceList.csv', 'ServiceDatesList.csv']
    for file in files:
        with open(file, 'r') as csv_file:                                        # Opens the 3 csv input files to the csv reader
            csv_reader = csv.reader(csv_file, delimiter=',')
            for line in csv_reader:                                              # Iterates through each line and extracts the data from the file 
                item_id = line[0]
                if file == files[0]:
                    items[item_id] = {}
                    man_name = line[1]
                    item_type = line[2]
                    damaged = line[3]
                    items[item_id]['manufacturer'] = man_name.strip()
                    items[item_id]['item_type'] = item_type.strip()
                    items[item_id]['damaged'] = damaged
                elif file == files[1]:
                    price = line[1]
                    items[item_id]['price'] = price
                elif file == files[2]:
                    service_date = line[1]
                    items[item_id]['service_date'] = service_date

    
    inventory = OutputInventory(items)                         # Creates all of the output files
    inventory.full()
    inventory.by_type()
    inventory.past_service()
    inventory.damaged()
    

    types = []                                                 # Extracts the different manufacturers and types, and puts them into a list
    manufacturers = []
    for item in items:
        checked_manufacturer = items[item]['manufacturer']
        checked_type = items[item]['item_type']
        if checked_manufacturer not in types:
            manufacturers.append(checked_manufacturer)
        if checked_type not in types:
            types.append(checked_type)
    
    
    user_input = None                                                           # The program then prompts the user for the user input
    while user_input != 'q':
        user_input = input("\nPlease enter an item manufacturer and item type (ex: Apple laptop) or enter 'q' to quit:\n")
        if user_input == 'q':                                                   # Allows the user to enter 'q' to quit
            break
        else:
            selected_manufacturer = None                                        # Checks each word from user to see if there is a match in manufacturer and item type
            selected_type = None
            user_input = user_input.split()
            bad_input = False
            for word in user_input:
                if word in manufacturers:
                    if selected_manufacturer:                                   # Checks to make sure input only has one submitted manufacturer
                        bad_input = True
                    else:
                        selected_manufacturer = word
                elif word in types:
                    if selected_type:                                           # Checks to see if only have one submitted type
                        bad_input = True
                    else:
                        selected_type = word
            if not selected_manufacturer or not selected_type or bad_input:
                print("No such item in inventory")
            else:                                                               # Uses ordered list of keys to iterate through based on highest price first
                def get_serviceprice(x):                                        # The get_serviceprice is used get order of keys to write to file based on price
                    return items[x]['price']
                keys = sorted(items.keys(), key=get_serviceprice)               # Gets the matching list of items based on user input
                matching_items = []
                similar_items = {}                                              # Stores items with same type but different manufacturer
                for item in keys:                                               # Item must match and be in inventory and not damaged or past service
                    if items[item]['item_type'] == selected_type:               
                        today = datetime.now().date()
                        service_date = items[item]['service_date']
                        service_expiration = datetime.strptime(service_date, "%m/%d/%Y").date()
                        expired = service_expiration < today
                        if items[item]['manufacturer'] == selected_manufacturer:       # Don't add damaged items or past service to matched list or similar list
                            if not expired and not items[item]['damaged']:
                                matching_items.append((item, items[item]))
                        else:
                            if not expired and not items[item]['damaged']:
                                similar_items[item] = items[item]
                                
                if matching_items:                                                # Outputs the items if matched
                    item = matching_items[0]
                    item_id = item[0]
                    man_name = item[1]['manufacturer']
                    item_type = item[1]['item_type']
                    price = item[1]['price']
                    print("Your item is: {}, {}, {}, {}\n".format(item_id, man_name, item_type, price))
                    
                    if similar_items:                                                         # Outputs item from different manufacturer that is closest in price to matched item
                        matched_price = price                                                 # Gets the similar item with the closest price to the initial item
                        closest_item = None
                        closest_price_diff = None
                        for item in similar_items:
                            if closest_price_diff == None:
                                closest_item = similar_items[item]
                                closest_price_diff = abs(int(matched_price) - int(similar_items[item]['price']))
                                item_id = item
                                man_name = similar_items[item]['manufacturer']
                                item_type = similar_items[item]['item_type']
                                price = similar_items[item]['price']
                                continue
                            price_diff = abs(int(matched_price) - int(similar_items[item]['price']))
                            if price_diff < closest_price_diff:
                                closest_item = item
                                closest_price_diff = price_diff
                                item_id = item
                                man_name = similar_items[item]['manufacturer']                      # Outputs the Items if they are the closer in price
                                item_type = similar_items[item]['item_type']
                                price = similar_items[item]['price']
                        print("You may, also, consider: {}, {}, {}, {}\n".format(item_id, man_name, item_type, price))
                    
                else:
                    print("No such item in inventory")                                              # Output if item isn't in inventory










