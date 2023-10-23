import pickle


def display_recipe(recipe):
    print(
        f"""recipe : {recipe["name"]}
        cooking time (min): {recipe['cooking_time']}
        ingredients: {" ".join(recipe["ingredients"])}
        difficulty level: {recipe['difficulty']}"""
    )


def search_ingredient(data):
    print("Here are all the available ingredients: ")
    for count, ingredient in enumerate(data["ingredients_list"]):
        print(count, ingredient)
    try:
        ingredient_searched = int(input("Please enter an ingredient number: "))
    except IndexError:
        print("Icorrect input, try again!")
    except:
        print("Something went wrong, please try again.")
    else:
        for recipe in data["recipes_list"]:
            if ingredient in recipe["ingredients"]:
                print(recipe)


recipe_file = input("Please enter name of the file including the extention: ")

try:
    user_recipe = open(recipe_file, "rb")
    data = pickle.load(user_recipe)
    # define var data structure?

except FileNotFoundError:
    print("File doesn't exist, exiting.")
    data = {"recipes_list": [], "ingredients_list": []}
except:
    print("an unexpecred error occurred.")
    data = {"recipes_list": [], "ingredients_list": []}
else:
    search_ingredient(data)
