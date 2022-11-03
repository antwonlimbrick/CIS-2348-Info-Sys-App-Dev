#Antwon Limbrick 1972657


new_list = []
user_input = input().split()

x = len(user_input)
for n in range(0, x):
    element = int(user_input[n])
    if element >= 0:
        new_list.append(element)

new_list.sort()
print(*new_list, end=" ")








