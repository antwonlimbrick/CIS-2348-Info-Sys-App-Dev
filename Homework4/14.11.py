#Antwon Limbrick 1972657


def selection_sort_descend_trace(num):
    for i in range(len(num) - 1):
        t = i
        for j in range(i + 1, len(num)):
            if num[t] < num[j]:
                t = j
        num[i], num[t] = num[t], num[i]
        for value in num:
            print(value,end=" ")
        print()
    return num

if __name__ == "__main__":
    num = []
    num = [int(x) for x in input("").split()]
    selection_sort_descend_trace(num)
