# Importing necessary modules from SQLAlchemy
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Set up SQLAlchemy Engine and Session
engine = create_engine("mysql://cf-python:password@localhost/my_database")
Session = sessionmaker(bind=engine)
session = Session()
# Creating the base class using declarative base for ORM
Base = declarative_base()


# Creates the data model for Recipes
class Recipe(Base):
    __tablename__ = "final_recipes"
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    ingredients = Column(String(250))
    cooking_time = Column(Integer)
    difficulty = Column(String(20))

    # representation methods for printing recipes
    def __repr__(self):
        return (
            "<Recipe ID: "
            + str(self.id)
            + "-"
            + self.name
            + "- Difficulty: "
            + self.difficulty
            + ">"
        )

    def __str__(self):
        return f"""
            -----------------------------
            Recipe ID: {self.id}
            Name: {self.name}
            Ingredients: {self.ingredients}
            Cooking time: {self.cooking_time}
            Difficulty: {self.difficulty}
            -----------------------------
        """

    def calculate_difficulty(self):
        ingredients_list = self.ingredients.split(", ")
        ingredients_num = len(ingredients_list)
        if self.cooking_time < 10 and ingredients_num < 4:
            self.difficulty = "Easy"
        elif self.cooking_time < 10 and ingredients_num >= 4:
            self.difficulty = "Medium"
        elif self.cooking_time >= 10 and ingredients_num < 4:
            self.difficulty = "Intermediate"
        else:
            self.difficulty = "Hard"

    def return_ingredients_as_list(self):
        if self.ingredients == "":
            return []
        else:
            ingredient_list = self.ingredients.split(", ")
            return ingredient_list


# Creating tables in the database based on the above class definition
print("Creating tables...")
Base.metadata.create_all(engine)
print("Tables created successfully.")


def create_recipe():
    name = input("Enter recipe name: ")
    if not name.strip() or len(name) > 50 or not name.replace(" ", "").isalpha():
        print(
            "Invalid recipe name. Please enter an alphabetic value of less than 50 characters"
        )
        name = input("Enter recipe name: ")
    cooking_time = input("Enter cooking time, in minutes: ")
    if not cooking_time.isnumeric() or not cooking_time.strip():
        print("Please enter a number")
        cooking_time = input("Enter cooking time, in minutes: ")
    ingredients = []
    ingredients_num_input = int(
        input("How many ingredients would you like to enter?: ")
    )
    for ingredient in range(ingredients_num_input):
        ingredient_input = input("Enter ingredients (one at a time): ")
        if (
            not ingredient_input.strip()
            or not ingredient_input.replace(" ", "").isalpha()
        ):
            print("Please enter an alphabetic value")
            ingredient_input = input("Enter ingredients (one at a time): ")
        if ingredient_input not in ingredients:
            ingredients.append(ingredient_input)

    ingredients_string = ", ".join(ingredients)

    print("Successfully added ingredients to the recipe.")

    recipe_entry = Recipe(
        name=name, ingredients=ingredients_string, cooking_time=int(cooking_time)
    )

    recipe_entry.calculate_difficulty()
    session.add(recipe_entry)
    session.commit()
    print("Recipe successfully created!")


def check_recipe():
    recipes_list = session.query(Recipe).all()
    if not recipes_list:
        print("There are no recipes available. Please create one.")
        return None


def view_all_recipes():
    check_recipe()
    recipes_list = session.query(Recipe).all()

    for recipe in recipes_list:
        print(recipe)


def search_by_ingredients():
    check_recipe()
    results = session.query(Recipe.ingredients).all()
    all_ingredients = []
    for ingredients in results:
        for ingredient_string in ingredients:
            ingredient_item = ingredient_string.split(", ")
            for ingredient in ingredient_item:
                if not ingredient in all_ingredients:
                    all_ingredients.append(ingredient)

    print("Here are all the available ingredients: \n")
    for index, ingredient in enumerate(all_ingredients, 1):
        print(index, ingredient)

    selection = input(
        "Enter ID of ingredient(s) to find available recipes \nIf you are entering multiple IDs, separate them with a comma: "
    )
    split_selection = selection.split(", ")
    for idx in split_selection:
        if int(idx) > len(all_ingredients) or int(idx) <= 0:
            print("Incorect selection, try again!")
            return None
    try:
        search_ingredients = [
            list(all_ingredients)[int(index) - 1]
            for index in split_selection
            if index.isdigit()
        ]
    except IndexError:
        print("Please enter a valid number:")
    conditions = [
        Recipe.ingredients.like("%" + ingredient + "%")
        for ingredient in search_ingredients
    ]

    recipes = session.query(Recipe).filter(*conditions).all()

    if not recipes:
        print("----------------\n\nNo recipes found!")
    else:
        for recipe in recipes:
            print("\nRecipe ID: " + str(recipe.id))
            print("Name: " + recipe.name)


def update_recipe():
    check_recipe()
    results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()

    for recipe in results:
        print(recipe)

    try:
        recipe_id_input = int(input("Enter recipe ID to update: "))
    except ValueError:
        print("Incorrect input, try again!")
    except:
        print("Something went wrong, please try again.")
    else:
        recipe_to_edit = session.get(Recipe, int(recipe_id_input))
        if not recipe_to_edit:
            print("Invalid selection")
            recipe_id_input = int(input("Enter recipe ID to update: "))

    print("1. Name\n2. Ingredients\n3. Cooking Time")
    edit_input = input("Enter the number of the attribute to edit: ")
    new_value = input("Enter the new value: ")
    if edit_input == "1":
        if not len(new_value) < 50 or not new_value.isalpha():
            print("Please enter a valid alphabetic value of less than 50 characters.")
        else:
            recipe_to_edit.name = new_value
    elif edit_input == "2":
        recipe_to_edit.ingredients = new_value
        recipe_to_edit.calculate_difficulty()

    elif edit_input == "3":
        if not new_value.isnumeric():
            print("Please enter a valid number.")
        else:
            recipe_to_edit.cooking_time == new_value
            recipe_to_edit.calculate_difficulty()
    else:
        print("Invalid entry, exiting.")
    session.commit()
    print("Successfully updated recipe")


def delete_recipe():
    check_recipe()
    results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()

    for recipe in results:
        print("\nRecipe ID: " + str(recipe[0]))
        print("Name: " + recipe[1])

    recipe_id_input = int(input("\nEnter recipe ID to delete: "))

    recipe_to_delete = session.query(Recipe).get(int(recipe_id_input))
    if not recipe_to_delete:
        print("Invalid selection")
        recipe_id_input = int(input("\nEnter recipe ID to delete: "))

    confirmation = input("Are you sure you want to delete this recipe? (y/n): ")
    if confirmation == "y":
        session.delete(recipe_to_delete)
        session.commit()
        print("Recipe deleted.")


def main_menu():
    choice = ""
    while choice != "exit":
        print("Pick an action: ")
        print("1. Create a new recipe")
        print("2. View all recipes")
        print("3. Search for an existing recipe")
        print("4. Update a recipe")
        print("5. Delete a recipe")
        print('type "exit" to exit the program.')
        choice = input("Your choice: ")

        if choice == "1":
            create_recipe()
        elif choice == "2":
            view_all_recipes()
        elif choice == "3":
            search_by_ingredients()
        elif choice == "4":
            update_recipe()
        elif choice == "5":
            delete_recipe()
        elif choice == "exit":
            print("\nGoodbye")
            session.close()
        else:
            print("Invalid selection")


main_menu()
