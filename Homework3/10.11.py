# Antwon Limbrick 1972657


class FoodItem:
    def get_calories(self, num_servings):
        # Calorie formula
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings;
        return calories

    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
        
    def __init__(self, item_name="None", amount_fat=0.0, amount_carbs=0.0, amount_protein=0.0):
        self.name = item_name
        self.fat = amount_fat
        self.carbs = amount_carbs
        self.protein = amount_protein

if __name__ == "__main__":
    f_item1 = FoodItem()
    item_name = input()
    amount_fat = float(input())
    amount_carbs = float(input())
    amount_protein = float(input())
    f_item2 = FoodItem(item_name, amount_fat, amount_carbs, amount_protein)
    num_servings = float(input())
    f_item1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,f_item1.get_calories(num_servings)))
    print()
    f_item2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings,f_item2.get_calories(num_servings)))





