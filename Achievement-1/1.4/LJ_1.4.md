1.	Why is file storage important when you’re using Python? What would happen if you didn’t store local files?

Storage is important in python because it allows data to be saved even after scripts stop running. If files weren't stored the data 
would simply be destroyed after each instance of the script being run.

2.	In this Exercise you learned about the pickling process with the pickle.dump() method. What are pickles? In which situations would you choose to use pickles and why? 

Pickles are methods by which simple text files are converted into binary files. this allows for the formatting of complex data structures,
such as dictionaries.

3.	In Python, what function do you use to find out which directory you’re currently in? What if you wanted to change your current working directory?

The function used for displaying the current directory is: os.getcwd()
To change directory: os.chdir('/path/to/directory')

4.	Imagine you’re working on a Python script and are worried there may be an error in a block of code. How would you approach the situation to prevent the entire script from terminating due to an error?

I would write a try except block, specifying what to do if an error occurs in the except block. I would also include a finally block to run code regardless of the outcome.

5.	You’re now more than halfway through Achievement 1! Take a moment to reflect on your learning in the course so far. How is it going? What’s something you’re proud of so far? Is there something you’re struggling with? What do you need more practice with? Feel free to use these notes to guide your next mentor call. 
I feel that I am still a little unclear with python syntax, and I find it sometimes difficult to follow the task instructions.
