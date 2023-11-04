class Recipe(object):
    all_ingredients = []

    def __init__(self, name):
        self.name = name
        self.ingredients = []
        self.cooking_time = int(0)
        self.difficulty = None

    def get_name(self):
        return self.name
    
    def get_cooking_time(self):
        return self.cooking_time

    def set_name(self, name):
        self.name = name

    def set_cooking_time(self, cooking_time):
        self.cooking_time = cooking_time
        self.calc_difficulty()

    def add_ingredients(self, *ingredients):
        self.ingredients.extend(ingredients)
        self.update_all_ingredients()
        self.calc_difficulty()

    def get_ingredients(self):
        return self.ingredients

    def get_dificulty(self):
        if not self.difficulty is None:
            self.calc_difficulty()
        return self.difficulty

    def update_all_ingredients(self):
        for ingredient in self.ingredients:
            if not ingredient in self.all_ingredients:
                Recipe.all_ingredients.append(ingredient)

    def __str__(self):
        output = (
            "\nRecipe name: "
            + str(self.name)
            + "\nIngredients: "
            + str(", ".join(self.ingredients))
            # + str(self.ingredients)
            + "\nCooking time: "
            + str(self.cooking_time)
            + "\nDifficulty: "
            + str(self.difficulty)
        )
        return output

    def calc_difficulty(self):
        ingredients_num = len(self.ingredients)
        if self.cooking_time < 10 and ingredients_num < 4:
            self.difficulty = "Easy"
        if self.cooking_time < 10 and ingredients_num >= 4:
            self.difficulty = "Medium"
        if self.cooking_time >= 10 and ingredients_num < 4:
            self.difficulty = "Intermediate"
        if self.cooking_time >= 10 and ingredients_num >= 4:
            self.difficulty = "Hard"

    def search_ingredient(self, ingredient):
        return ingredient in self.ingredients


def recipe_search(data: list(Recipe), search_term):
    for recipe in data:
        if recipe.search_ingredient(search_term):
            print("recipe that contain your search term: ", search_term, "\n", recipe)
            # print(recipe)


tea = Recipe("Tea")
tea.get_cooking_time()
tea.add_ingredients("Tea Leaves", "Sugar", "Water")
tea.set_cooking_time(5)
tea.get_dificulty()
print(tea)

coffee = Recipe("Coffee")
coffee.add_ingredients("Coffee Powder", "Sugar", "Water")
coffee.set_cooking_time(5)
coffee.get_dificulty()
print(coffee)

cake = Recipe("Cake")
cake.add_ingredients(
    "Sugar", "Butter", "Eggs", "Vanilla Essence", "Flour", "Baking Powder", "Milk"
)
cake.set_cooking_time(50)
cake.get_dificulty()
print(cake)

banana_smoothie = Recipe("Banana Smoothie")
banana_smoothie.add_ingredients(
    "Bananas", "Milk", "Peanut Butter", "Sugar", "Ice Cubes"
)
banana_smoothie.set_cooking_time(5)
banana_smoothie.get_dificulty()
print(banana_smoothie)

recipes_list = [tea, coffee, cake, banana_smoothie]

search_list = ["Water", "Sugar", "Bananas"]

for ingredient in search_list:
    recipe_search(recipes_list, ingredient)
