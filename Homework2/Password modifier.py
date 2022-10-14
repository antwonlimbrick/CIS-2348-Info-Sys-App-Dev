#Antwon Limbrick
#1972657

user_password = input()


for character in user_password:                 
    if character == 'i':               
        user_password = user_password.replace('i', '!')
    elif character == 'a':             
        user_password = user_password.replace('a', '@')
    elif character == 'm':             
        user_password = user_password.replace('m', 'M')
    elif character == 'B':             
        user_password = user_password.replace('B', '8')
    elif character == 'o':             
        user_password = user_password.replace('o', '.')
else:                                  
    user_password += 'q*s'

print(user_password)
