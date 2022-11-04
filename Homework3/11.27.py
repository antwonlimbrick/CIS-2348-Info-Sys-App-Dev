#Antwon Limbrick 1972657

from collections import OrderedDict


i=1
count=1
roster_dict = {}
for i in range(1,6):
    jersey = int(input('Enter player {}\'s jersey number:\n' .format(i)))
    rating = int(input('Enter player {}\'s rating:\n' .format(i)))
    print()
    roster_dict[jersey] = rating
    
if jersey < 0 or jersey > 99 or rating < 0 or rating > 9:
    print('invalid entry')
else:
    roster_dict = OrderedDict(sorted(roster_dict.items()))
    print("ROSTER")
    i=1
    for a,b in roster_dict.items():
        print("Jersey number: %d, Rating: %d" % (a, b))




menu_option = ''

while menu_option != 'q':
    print('\nMENU\na - Add player\nd - Remove player\nu - Update player rating\nr - Output players above a rating\no - Output roster\nq - Quit\n')
    menu_option = input('Choose an option:')
    if menu_option == 'a':
        jersey = int(input('Enter a new player\'s jersey number:\n' .format(i)))
        rating = int(input('Enter the players\'s rating:\n' .format(i)))
        roster_dict[jersey] = rating
        
    elif menu_option == 'd':
        jersey = int(input('Enter a jersey number:\n'))
        if jersey in roster_dict.keys():
            del roster_dict[jersey]
        
    elif menu_option == 'u':
        jersey = int(input('Enter a jersey number:\n'))
        if jersey in roster_dict.keys():
            rating = int(input('Enter a new rating for player:\n'))
            roster_dict[jersey] = rating
    
    elif menu_option == 'r':
        num = int(input('Enter a rating:\n'))
        print('ABOVE {}'.format(num))
        #sorted_roster = sorted(roster_dict.keys())
        if rating in roster_dict[jersey] > num:
            for a,b in roster_dict.items():
                print("Jersey number: %d, Rating: %d" % (a, b))
    
    elif menu_option == 'q':
        print()
    
    else:
        print('invalid entry')



