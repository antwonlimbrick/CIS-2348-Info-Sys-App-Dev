import math


height = int(input("Enter wall height (feet):\n"))

width = int(input("Enter wall width (feet):\n"))

area = height * width

print("Wall area:", area ,"square feet")

paint_needed = float(area/350)

print("Paint needed: %.2f" %paint_needed,"gallons")

gallons_needed = 1

cans_needed = int(math.ceil(paint_needed/gallons_needed))

print("Cans needed:", cans_needed, "can(s)")

paintColors = {
    'red':35,
    'blue':25,
    'green':23
}

print()

color_choice = input("Choose a color to paint the wall:\n")

print("Cost of purchasing", color_choice, "paint: $"+str(paintColors[color_choice] * cans_needed))


