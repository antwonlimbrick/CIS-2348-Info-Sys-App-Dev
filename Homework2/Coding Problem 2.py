#Antwon Limbrick
#1972657


def get_month(monthString):
        if monthString == 'January':
            month = 1
        elif monthString == 'February':
            month= 2
        elif monthString == 'March':
            month = 3
        elif monthString == 'April':
            month = 4
        elif monthString == 'May':
            month = 5
        elif monthString == 'June':
            month = 6
        elif monthString == 'July':
            month = 7
        elif monthString == 'August':
            month = 8
        elif monthString == 'September':
            month = 9
        elif monthString == 'October':
            month = 10
        elif monthString == 'November':
            month = 11
        elif monthString == 'December':
            month = 12
        else:
            month = 0
        return month

input_file=open("inputDates.txt", 'r')

user_string = input()
    
if __name__ == '__main__':
    string1=[]
    string2=[]
    while input_file != "-1":
        string1.append(input_file)
        input_file = input()
    for i in string1:
        if len(i.split()) > 1:
            if ',' in i.split()[1]:
                print('{}/{}/{}'.format(get_month(i.split()[0]), i.split()[1][:-1], i.split()[2]))
                
                

