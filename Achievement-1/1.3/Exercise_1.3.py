recipes_list = []
ingredients_list = set()

n = int(input("how many recipes would you like to define?"))


def take_recipe(*recipe):
    name = input("Enter recipe name:")
    cooking_time = int(input("Enter cooking time in minutes:"))
    ingredients = list(input("Enter ingredients list:").split())
    recipe = {"name": name, "cooking_time": cooking_time, "ingredients": ingredients}
    return recipe


for recipe in range(0, n):
    recipe = take_recipe()
    recipes_list.append(recipe)
    # ingredients = [ ingredient for ingredient in recipe['ingredients'] if ingredient not in ingredients_list]
    for ingredient in recipe["ingredients"]:
        if not ingredient in ingredients_list:
            ingredients_list.add(ingredient)

for recipe in recipes_list:
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) < 4:
        difficulty = "Easy"
    if recipe["cooking_time"] < 10 and len(recipe["ingredients"]) >= 4:
        difficulty = "Medium"
    if recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) < 4:
        difficulty = "Intermediate"
    if recipe["cooking_time"] >= 10 and len(recipe["ingredients"]) >= 4:
        difficulty = "Hard"
    print(
        "recipe :",
        recipe["name"],
        "\n",
        "cooking time (min): ",
        recipe["cooking_time"],
        "\n",
        "ingredients: ",
        " ".join(recipe["ingredients"]),
        "\n",
        "difficulty level: ",
        difficulty,
    )

sorted_ingredients = sorted(ingredients_list)
print("ingredients available across all recipes: ", " ".join(sorted_ingredients))
