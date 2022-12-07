#Antwon Limbrick 1972657



num_calls = 0


def partition(ids_names, i, x):
    move = ids_names[x] 
    index = i - 1
    for j in range(i, x):
        if ids_names[j] <= move:
            index += 1
            ids_names[index], ids_names[j] = ids_names[j], ids_names[index]
    ids_names[index+1], ids_names[x] = ids_names[x], ids_names[index+1]
    return index+1

def quicksort(ids_names, i, x):
    if i < x:
        piv = partition(ids_names, i, x)
        quicksort(ids_names, i, piv-1)
        quicksort(ids_names, piv+1, x)

if __name__ == "__main__":
    ids_names = []
    user_id = input()
    while user_id != "-1":
        ids_names.append(user_id)
        user_id = input()
    quicksort(ids_names, 0, len(ids_names) - 1)
    num_calls = int(2 * len(ids_names) - 1)
    print(num_calls)
    for user_id in ids_names:
        print(user_id)




