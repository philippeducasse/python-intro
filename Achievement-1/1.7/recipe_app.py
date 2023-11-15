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
        return (
            "-----------------------------\n"
            f"Recipe ID: {self.id}\n"
            f"Name: {self.name}\n"
            f"Ingredients: {self.ingredients}\n"
            f"Cooking time: {self.cooking_time}\n"
            f"Difficulty: {self.difficulty}\n"
            "-----------------------------\n"
        )

    def calculate_difficulty(self):
        ingredients_list = self.ingredients.split(", ")
        ingredients_num = len(ingredients_list)
        if self.cooking_time < 10 and ingredients_num < 4:
            return "Easy"
        elif self.cooking_time < 10 and ingredients_num >= 4:
            return "Medium"
        elif self.cooking_time >= 10 and ingredients_num < 4:
            return "Intermediate"
        else:
            return "Hard"

    def return_ingredients_as_list(self):
        if self.ingredients == "":
            return ""
        else:
            ingredient_list = self.ingredients.split(", ")
            return ingredient_list


# Creating tables in the database based on the above class definition
print("Creating tables...")
Base.metadata.create_all(engine)
print("Tables created successfully.")


def create_recipe():
    name = str(input("Enter recipe name: "))
    cooking_time = str(input("Enter cooking time, in minutes: "))

    ingredients_input = input(
        "Ingredients of the recipe (separate them with comma(,) and space ( ): "
    )
    if len(name) > 50 or not name.isalnum():
        print(
            "Invalid recipe name. Please enter an alphanumeric value of less than 50 characters"
        )
        return
    if not cooking_time.isnumeric():
        print("Please enter a number")
        return

    recipe_entry = Recipe(
        name=name, ingredients=ingredients_input, cooking_time=int(cooking_time)
    )

    recipe_entry.difficulty = recipe_entry.calculate_difficulty()
    session.add(recipe_entry)
    session.commit()
    print("Recipe successfully created!")


def view_all_recipes():
    recipes_list = session.query(Recipe).all()
    if not recipes_list:
        print("There are no recipes available. Please create one.")
        return None

    for recipe in recipes_list:
        print(recipe.__str__)


def search_recipe():
    number_of_recipes = session.query(Recipe).count()
    if number_of_recipes == 0:
        print("There are no recipes available. Please create one.")
        return None
    else:
        results = session.query(Recipe.ingredients).all()
        breakpoint()
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
        "Enter ID of ingredient(s) to find available recipes \n If you are entering multiple IDs, separate them with a comma: "
    )
    ingredient_index = selection.split(", ")
    search_ingredients = [
        list(all_ingredients)[int(index) - 1]
        for index in ingredient_index
        if index.isdigit()
    ]
    conditions = [
        Recipe.ingredients.like("%" + ingredient + "%")
        for ingredient in search_ingredients
    ]

    # conditions = []

    # for ingredient in search_ingredients:
    #     like_term = '%' + ingredient + '%'
    #     conditions.append(like_term)

    recipes = selection.query(Recipe).filter(*conditions).all()

    for recipe in recipes:
        print(recipe.__str__)


def update_recipe():
    number_of_recipes = session.query(Recipe).count()
    if number_of_recipes == 0:
        print("There are no recipes available. Please create one.")
        return None
    results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()

    for recipe in results:
        print(recipe)

    try:
        recipe_id_input = input("Enter recipe ID to update: ")
    except IndexError:
        print("Incorrect input, try again!")
    except:
        print("Something went wrong, please try again.")
    else:
        recipe_to_edit = session.query(Recipe.id.like(recipe_id_input))
        print(
            "---------------------\n"
            f"1 - Name: {recipe_to_edit.name}\n"
            f"2 - Ingredients: {recipe_to_edit.ingredients}\n"
            f"3 - Cooking time: {recipe_to_edit.cooking_time}\n"
            "\n"
        )
        edit_input = input("Enter the number of the attribute to edit: ")
        new_value = input("Enter the new value: ")
        if edit_input == "1":
            recipe_to_edit.name = new_value
        elif edit_input == "2":
            recipe_to_edit.ingredients = new_value
        elif edit_input == "3":
            recipe_to_edit.cooking_time == new_value
        else:
            print("Invalid entry, exiting.")

        recipe_to_edit.difficulty = recipe_to_edit.calculate_difficulty()
        session.commit()
        print("Successfully updated recipe")


def delete_recipe():
    number_of_recipes = session.query(Recipe).count()
    if number_of_recipes == 0:
        print("There are no recipes available. Please create one.")
        return None

    results = session.query(Recipe).with_entities(Recipe.id, Recipe.name).all()

    for recipe in results:
        print(recipe)

    try:
        recipe_id_input = input("Enter recipe ID to delete: ")
    except IndexError:
        print("Incorrect input, try again!")
    except:
        print("Something went wrong, please try again.")
    else:
        recipe_to_delete = session.query(Recipe).get(int(recipe_id_input))
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
        print("2. Search for an existing recipe")
        print("3. Update a recipe")
        print("4. Delete a recipe")
        print('type "exit" to exit the program.')
        choice = input("Your choice: ")

        if choice == "1":
            create_recipe()
        elif choice == "2":
            search_recipe()
        elif choice == "3":
            update_recipe()
        elif choice == "4":
            delete_recipe()
        elif choice == "exit":
            session.commit()
            session.close()
            engine.close()
        else:
            print("Invalid selection")


main_menu()
