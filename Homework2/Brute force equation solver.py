
#Antwon Limbrick
#1972657

num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())
num6 = int(input())
signal = True

for x in range(-10, 10):
    for y in range(-10, 10):
       if num1 * x + num2 * y == num3 and num4 * x + num5 * y == num6:
           signal = False
           print(x, y)
if signal == True:
    print('No solution')
