recipes_list = []
ingredients_list = []

n = int(input("how many recipes would you like to define?"))


def take_recipe(*recipe):
    name = input("Enter recipe name:")
    cooking_time = int(input("Enter cooking time in minutes:"))
    ingredients = list(input("Enter ingredients seperated by a comma and space:").lower().split(", "))
    recipe = {"name": name, "cooking_time": cooking_time, "ingredients": ingredients}
    return recipe


for recipe in range(0, n):
    recipe = take_recipe()
    recipes_list.append(recipe)
    for ingredient in recipe["ingredients"]:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)

for recipe in recipes_list:
    cooking_time = recipe["cooking_time"]
    ing_length = len(recipe["ingredients"])

    if cooking_time < 10 and ing_length < 4:
        difficulty = "Easy"
    if cooking_time < 10 and ing_length >= 4:
        difficulty = "Medium"
    if cooking_time >= 10 and ing_length < 4:
        difficulty = "Intermediate"
    if cooking_time >= 10 and ing_length >= 4:
        difficulty = "Hard"
    print(
        f"""recipe : {recipe["name"]}
        cooking time (min): {cooking_time}
        ingredients: {" ".join(recipe["ingredients"])}
        difficulty level: {difficulty}"""
    )

sorted_ingredients = sorted(ingredients_list)

print("Ingredients available across all recipes: ")
for ing in sorted_ingredients:
    print(ing)
