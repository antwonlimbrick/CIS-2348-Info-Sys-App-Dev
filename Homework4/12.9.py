#Antwon Limbrick 1972657


chunks = input().split()
names = chunks[0]

while names != '-1':
    try:
        age = int(chunks[1]) + 1
        print('{} {}'.format(names, age))
        
    except ValueError:
        print('{} {}'.format(names, 0))
        
    chunks = input().split()
    names = chunks[0]




