first_num = input("enter a number: ")
second_num = input("enter another number: ")
operation = input("enter'+' or '-' to add or substract")

a = int(first_num)
b = int(second_num)

if operation == "+" :
    print("The sum of both numbers is: ", a + b)
elif operation == "-" :
    print("The difference between the first and second number is: ", a - b)
else:
    print("Please enter a valid operator")