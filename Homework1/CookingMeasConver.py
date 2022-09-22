
lem_juice = float(input("Enter amount of lemon juice (in cups):\n"))

water = float(input("Enter amount of water (in cups):\n"))

agave_nec = float(input("Enter amount of agave nectar (in cups):\n"))

servings = float(input("How many servings does this make?\n"))

print()

print("Lemonade ingredients - yields {:.2f} servings".format(servings))

print("{:.2f} cup(s) lemon juice".format(lem_juice))

print("{:.2f} cup(s) water".format(water))

print("{:.2f} cup(s) agave nectar".format(agave_nec))

print()


servings_num = float(input("How many servings would you like to make?\n"))

print()

fac_num = servings_num / servings

print("Lemonade ingredients - yields {:.2f} servings".format(servings_num))

print("{:.2f} cup(s) lemon juice".format(lem_juice * fac_num))

print("{:.2f} cup(s) water".format(water * fac_num))

print("{:.2f} cup(s) agave nectar".format(agave_nec * fac_num))

print()


print("Lemonade ingredients - yields {:.2f} servings".format(servings_num))

print("{:.2f} gallon(s) lemon juice".format(lem_juice * fac_num / 16))

print("{:.2f} gallon(s) water".format(water * fac_num / 16))

print("{:.2f} gallon(s) agave nectar".format(agave_nec * fac_num / 16))




