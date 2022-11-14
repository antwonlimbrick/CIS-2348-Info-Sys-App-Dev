#Antwon Limbrick 1972657
#Final Project Part 1

import csv                                              #Import of csv module
import datetime                                         #Import of daytime library


with open('ManufacturerList.csv','r') as file:          #Program opens and reads ManufacturerList
    data = csv.reader(file)

    item_list = []                                      #Creates the manufacture list
    
    for data_row in data:                               #Loop appends each row into list
        item_list.append(data_row)

    
with open('PriceList.csv', 'r') as file:                #Opens Price List and reads data
    data = csv.reader(file)
    
    for data_row in data:                               #Loop searches the price list by item ID and appends the price
        for a in range( len(item_list) ):
            if(item_list[a][0] == data_row[0]):
                item_list[a].append( data_row[1] )

with open('ServiceDatesList.csv', 'r') as file:           #Opens Service Dates List and reads into data
    data = csv.reader(file)

    for data_row in data:                                 #Loop searches index of item ID and appends the service dates
        for a in range( len(item_list) ):
            if(item_list[a][0] == data_row[0]):
                item_list[a].append( data_row[1] )



for a in range( len(item_list) - 1 ):                     #Sorting in alphabetical order starts
    for b in range(len(item_list) - 1 - a):               #Temperary values converted into lowercase to sort easier
        x = item_list[b][1].lower()
        y = item_list[b+1][1].lower()
        
        if(ord(x[0]) > ord(y[0])):                        #Using ord to return the ascii values of the letters in string and swaps if not in alphabetical order
            temp = item_list[b]                           #Temp is used as a temperary valuse 
            item_list[b] = item_list[b+1]
            item_list[b+1] = temp
        
        else:
            i = 0
            
            while(ord(x[i]) == ord(y[i]) and len(x) > i+1 and len(y) > i + 1):
                i=i+1

                if(ord(x[i]) >= ord(y[i]) and len(x) > len(y) ):        #Swaps the values if they're not in alphabetical order
                    temp = item_list[b]
                    item_list[b] = item_list[b+1]
                    item_list[b+1] = temp



with open('FullInventory.csv', 'w', newline='') as file:            #Opens an new file to write list of items into FullInventory.csv file
    writer = csv.writer(file, delimiter='|')
    data = []
    for a in range( len(item_list)):
        data.append( [ item_list[a][0], item_list[a][1], item_list[a][2], item_list[a][4], item_list[a][5], item_list[a][3] ])
        writer.writerows(data)

#^ ^ ^ ^ Every Line above is for Part A output ^ ^ ^ ^


for a in range( len(item_list) - 0 ):                        #Sorting item ID in order starts
    for b in range(len(item_list) - 0 - a):                  #Temperary values used
        x = item_list[b][0]
        y = item_list[b+0][0]
        
        if((x[0]) > (y[0])):                                #Statement swaps if item ID not grater than values 
            temp = item_list[b]                             #Temp is used as a temperary values 
            item_list[b] = item_list[b+1]
            item_list[b+1] = temp
        
        else:
            i = 0
            
            while((x[i]) == (y[i]) and len(x) > i+1 and len(y) > i + 1):
                i=i+1

            if((x[i]) >= (y[i]) and len(x) > len(y) ):        #Swaps the values if item ID not grater than the other value
                temp = item_list[b]
                item_list[b] = item_list[b+1]
                item_list[b+1] = temp

with open('PhoneInventory.csv', 'w', newline='') as file:            #Opens an new file to write list of items that have a item type = Phone
    writer = csv.writer(file, delimiter='|')
    data = []
    for a in range( len(item_list)):
        if (item_list[a][2] == 'phone'):
            data.append( [ item_list[a][0], item_list[a][1], item_list[a][4], item_list[a][5], item_list[a][3] ])
            writer.writerows(data)
        else:
            continue

with open('LaptopInventory.csv', 'w', newline='') as file:           #Opens an new file to write list of items that have a item type = Laptop
    writer = csv.writer(file, delimiter='|')
    data = []
    for a in range( len(item_list)):
        if (item_list[a][2] == 'laptop'):
            data.append( [ item_list[a][0], item_list[a][1], item_list[a][4], item_list[a][5], item_list[a][3] ])
            writer.writerows(data)
        else:
            continue


with open('TowerInventory.csv', 'w', newline='') as file:            #Opens an new file to write list of items that have a item type = Tower
    writer = csv.writer(file, delimiter='|')
    data = []
    for a in range( len(item_list)):
        if (item_list[a][2] == 'tower'):
            data.append( [ item_list[a][0], item_list[a][1], item_list[a][4], item_list[a][5], item_list[a][3] ])
            writer.writerows(data)
        else:
            continue

#^ ^ ^ ^ Every Line above is for Part B output ^ ^ ^ ^


for a in range( len(item_list) - 5 ):                        #Sorting item Service Date in order starts
    for b in range(len(item_list) - 5 - a):                  #Temperary values used
        x = item_list[b][5]
        y = item_list[b+5][5]
        
        currentDay = datetime.datetime.now()
        
        if((x[5]) > currentDay.strftime("%m/%d/%Y")):       #Statement swaps if item Service date not grater than current Date 
            temp = item_list[b]                             #Temp is used as a temperary values 
            item_list[b] = item_list[b+1]
            item_list[b+1] = temp
        
        else:
            i = 0
            
            while((x[i]) == (y[i]) and len(x) > i+1 and len(y) > i + 1):
                i=i+1

            if((x[i]) >= currentDay.strftime("%m/%d/%Y") and len(x) > len(y) ):        #Swaps the values if Service Date not grater than the other value
                temp = item_list[b]                                                    #Puts them in order from Oldest to most Recent
                item_list[b] = item_list[b+1]
                item_list[b+1] = temp


with open('PastServiceDateInventory.csv', 'w', newline='') as file:            #Opens an new file to write list of items into FullInventory.csv file
    writer = csv.writer(file, delimiter='|')
    data = []
    for a in range( len(item_list)):
        data.append( [ item_list[a][0], item_list[a][1], item_list[a][2], item_list[a][4], item_list[a][5], item_list[a][3] ])
        writer.writerows(data)

#^ ^ ^ ^ Every Line above is for Part C output ^ ^ ^ ^



with open('DamagedInventory.csv', 'w', newline='') as file:            #Opens an new file to write list of items that have damaged
    writer = csv.writer(file, delimiter='|')
    data = []
    for a in range( len(item_list)):
        if (item_list[a][3] == 'damaged'):
            data.append( [ item_list[a][0], item_list[a][1], item_list[a][4], item_list[a][5], item_list[a][3] ])
            writer.writerows(data)
        else:
            continue

#^ ^ ^ ^ Every Line above is for Part D output ^ ^ ^ ^













