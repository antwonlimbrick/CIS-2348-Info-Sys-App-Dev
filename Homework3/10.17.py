#Antwon Limbrick 1972657


class ItemToPurchase:
    def __init__(self, item_name= 'none', item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_price = item_price
        self.item_quantity = item_quantity
        
    def print_item_cost(self):
        print(self.item_name, end = ' ')
        print(self.item_quantity, '@ $', end = '') 
        print(f'{self.item_price:.0f}', '= $', end ='')
        print(f'{self.item_quantity * self.item_price:.0f}')

if __name__ == "__main__": 
        print('Item 1')
        item1 = ItemToPurchase() 
        item1.item_name = input('Enter the item name:\n') 
        item1.item_price = float(input('Enter the item price:\n'))
        item1.item_quantity = int(input('Enter the item quantity:\n'))
        print()
        
        print('Item 2')
        item2 = ItemToPurchase() 
        item2.item_name = input('Enter the item name:\n') 
        item2.item_price = float(input('Enter the item price:\n')) 
        item2.item_quantity = int(input('Enter the item quantity:\n')) 
        
        total_cost = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
        
        print('TOTAL COST') 
        print(item1.print_item_cost(), '\n') 
        print(item2.print_item_cost(), '\n') 
        print('Total:','$',end = '')
        print(f'{total_cost:.0f}') 



