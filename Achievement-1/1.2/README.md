
    name (str): Contains the name of the recipe
    cooking_time (int): Contains the cooking time in minutes
    ingredients (list): Contains a number of ingredients, each of the str data type


Recipe 1 is a dictionary, as it contains 3 different key value pairs. The name is a string because it contains letters and refers to a word, while the cooking_time is a number because this will allow sorting by numerical order. Finally, the ingredients are a list because it contains various entries which we want to be able to modify with ease if needed.

all_recipes = [ ]

I have decided to use a list as the outer structure to store the recipe dictionaries because lists are sequential and can store multiple recipes that can be modified if needed.

