import pickle

recipes_list = []
ingredients_list = []


def take_recipe(*recipe):
    name = input("Enter recipe name: ")
    cooking_time = int(input("Enter cooking time in minutes: "))
    ingredients = list(
        input("Enter ingredients seperated by a comma and space: ").lower().split(", ")
    )
    difficulty = calc_difficulty(
        cooking_time, ingredients
    )  # this isn't getting appended to recipe

    recipe = {
        "name": name,
        "cooking_time": cooking_time,
        "ingredients": ingredients,
        "difficulty": difficulty,
    }
    return recipe


def calc_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    if cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    if cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    if cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = "Hard"
    return difficulty


user_file = input("Please enter a file name (without the extention): ") + ".bin"

try:
    user_recipe = open(user_file, "rb")
    data = pickle.load(user_recipe)

except FileNotFoundError:
    print("File doesn't exist, creating.")
    data = {
        "recipes_list": recipes_list,
        "ingredients_list": ingredients_list,
    }
except:
    print("an unexpecred error occurred.")
    data = {"recipes_list": recipes_list, "ingredients_list": ingredients_list}
else:
    user_file.close()
finally:
    recipes_list.extend(data["recipes_list"])
    print("File contains these recipes: " + str(recipes_list))
    ingredients_list.extend(data["ingredients_list"])
    print("file contains these ingredients: " + str(ingredients_list))

n = int(input("how many recipes would you like to define?"))

for recipe in range(0, n):
    recipe = take_recipe()
    recipes_list.append(recipe)
    for ingredient in recipe["ingredients"]:
        if not ingredient in ingredients_list:
            ingredients_list.append(ingredient)

print("This is the updated recipe file, with the new added recipe(s): " + str(data))

my_file = open(user_file, "wb")
pickle.dump(data, my_file)
my_file.close()

# print("Ingredients available across all recipes: ")
# for ing in sorted_ingredients:
#         print(ing)
