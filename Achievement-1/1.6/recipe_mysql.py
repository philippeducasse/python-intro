import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="cf-python",
    passwd="password",
)

cursor = conn.cursor(buffered=True)

cursor.execute("CREATE DATABASE IF NOT EXISTS task_database")
cursor.execute("USE task_database")

cursor.execute(
    """CREATE TABLE IF NOT EXISTS Recipes(
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(50),
    ingredients VARCHAR(255),
    cooking_time INT,
    difficulty VARCHAR(20)
)"""
)


def create_recipe(conn, cursor):
    ingredients_list = []
    name = str(input("Enter recipe name: "))
    cooking_time = int(input("Enter cooking time, in minutes: "))
    ingredients = input(
        "Ingredients of the recipe (separate them with comma(,) and space ( ): "
    )
    ingredients_list.append(ingredients)
    ingredients_str = ", ".join(ingredients_list)
    difficulty = calculate_difficulty(cooking_time, ingredients)
    sql = "INSERT INTO Recipes (name, ingredients, cooking_time, difficulty) VALUES(%s, %s, %s, %s)"
    val = (name, ingredients_str, cooking_time, difficulty)

    cursor.execute(sql, val)
    conn.commit()
    print("Recipe saved to the database")


def display_recipe(recipe):
    print("\nID:", recipe[0])
    print("Name:", recipe[1])
    print("Ingredients:", recipe[2])
    print("Cooking Time (mins):", recipe[3])
    print("Difficulty:", recipe[4])
    print("")


def calculate_difficulty(cooking_time, ingredients):
    if cooking_time < 10 and len(ingredients) < 4:
        difficulty = "Easy"
    elif cooking_time < 10 and len(ingredients) >= 4:
        difficulty = "Medium"
    elif cooking_time >= 10 and len(ingredients) < 4:
        difficulty = "Intermediate"
    elif cooking_time >= 10 and len(ingredients) >= 4:
        difficulty = "Hard"
    return difficulty


def search_recipe(conn, cursor):
    all_ingredients = []
    cursor.execute("""SELECT ingredients FROM Recipes""")
    # returns every SQL query
    results = cursor.fetchall()
    for ingredient_list in results:
        for ingredient in ingredient_list:
            ingredient_split = ingredient.split(", ")
            for ingredient_item in ingredient_split:
                ingredient_item = ingredient_item.strip()
                if not ingredient_item in all_ingredients:
                    all_ingredients.append(ingredient_item)

    print("Here are all the available ingredients: ")
    for count, ingredient in enumerate(all_ingredients, 1):
        print(count, ingredient)
    try:
        index = int(input("Please enter an ingredient number: ")) - 1
        ingredient_searched = all_ingredients[index]
        print("You selected: ", ingredient_searched)
    except IndexError:
        print("Icorrect input, try again!")
    except:
        print("Something went wrong, please try again.")
    else:
        sql = "SELECT * FROM Recipes WHERE Ingredients LIKE %s"
        val = ("%" + ingredient_searched + "%",)
        cursor.execute(sql, val)
        recipe_results = cursor.fetchall()

    for recipe in recipe_results:
        print("-------------------------------")
        print("\nRecipe name:", recipe[1])
        print("Cooking time (in minutes):", recipe[3])
        print("Difficulty:", recipe[4])
        ingredient_list = recipe[2].split(", ")
        print("Ingredients:")
        for ingredient in ingredient_list:
            print("- ", ingredient)
        print("-------------------------------")


def update_recipe(conn, cursor):
    view_recipes(conn, cursor)

    selectedRecipe = str(input("Enter recipe ID: "))

    sql = "SELECT * FROM Recipes WHERE id LIKE %s"
    val = ("%" + selectedRecipe + "%",)
    cursor.execute(sql, val)

    selectedUpdate = str(
        input("Enter key you want to update (name, coooking_time, ingredients): ")
    )
    newInput = input("Enter a new value: ")

    if selectedUpdate == "name":
        cursor.execute(
            f"UPDATE Recipes SET name = %s WHERE id = %s", (newInput, selectedRecipe)
        )
    elif selectedUpdate == "cooking_time":
        cursor.execute(
            f"UPDATE Recipes SET cooking_time = %s WHERE id = %s",
            (
                newInput,
                selectedRecipe,
            ),
        )
        update_difficulty(selectedRecipe)
    elif selectedUpdate == "ingredients":
        cursor.execute(
            f"UPDATE Recipes SET ingredients = %s WHERE id = %s",
            (
                newInput,
                selectedRecipe,
            ),
        )
        update_difficulty(selectedRecipe)
        print("Updated recipe successfully.")
    else:
        print("Invalid selection")

    conn.commit()


def update_difficulty(id):
    cursor.execute(f"SELECT * FROM Recipes WHERE id = %s", (id,))
    recipe_to_update = cursor.fetchall()

    ingredients = tuple(recipe_to_update[0][2].split(","))
    cooking_time = recipe_to_update[0][3]

    updated_difficulty = calculate_difficulty(cooking_time, ingredients)
    print("Updated difficulty:", updated_difficulty)
    cursor.execute(
        f"UPDATE Recipes SET difficulty = %s WHERE id = %s", (updated_difficulty, id)
    )


## View Recipes
def view_recipes(conn, cursor):
    print("\nAll Recipes:\n" + 20 * "-")

    cursor.execute(f"SELECT * FROM Recipes")
    results = cursor.fetchall()

    if len(results) == 0:
        print("\nNo recipes. Back to main menu.\n")
        return
    else:
        for row in results:
            display_recipe(row)


def delete_recipe(conn, cursor):
    view_recipes(conn, cursor)

    selectedRecipe = (input("Enter recipe ID: "),)

    # sql = "DELETE * FROM Recipes WHERE id = %s"
    # val = ("%" + selectedRecipe + "%",)
    sql = "DELETE FROM Recipes WHERE id = %s"
    cursor.execute(sql, selectedRecipe)

    conn.commit()
    print("\nRecipe was deleted successfully.")
    return


def main_menu(conn, cursor):
    choice = ""
    while choice != "exit":
        print("Pick an action: ")
        print("1. Create a new recipe")
        print("2. Search for an existing recipe")
        print("3. Update a recipe")
        print("4. Delete a recipe")
        print('type "exit" to exit the program.')
        choice = input("Your choice: ")

        if choice == "1":
            create_recipe(conn, cursor)
        elif choice == "2":
            search_recipe(conn, cursor)
        elif choice == "3":
            update_recipe(conn, cursor)
        elif choice == "4":
            delete_recipe(conn, cursor)
        elif choice == "exit":
            conn.commit()
            conn.close()
        else:
            print("Invalid selection")


main_menu(conn, cursor)
