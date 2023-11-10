# Python program for simple calculator

# Function to add two numbers
def add(num1, num2):
	return num1 + num2

# Function to subtract two numbers
def subtract(num1, num2):
	return num1 - num2

# Function to multiply two numbers
def multiply(num1, num2):
	return num1 * num2

# Function to divide two numbers
def divide(num1, num2):
	check_divide_by_zero(num2)
	return num1 / num2

def is_number(s):
    while s.isdigit() == False:
        s = input("Enter only numbers: ")
    return int(s)

def check_divide_by_zero(s):
    while int(s) == 0:
        s = input("You can't divide by Zero: ")
    return int(s)

def check_operation_number(s):
    if s.isdigit() and int(s) >= 1 and int(s) <= 4:
        return int(s)
    else:
        return 0




print("Please select operation -\n" \
		"1. Add\n" \
		"2. Subtract\n" \
		"3. Multiply\n" \
		"4. Divide\n")


# Take input from the user
select_operation_type = check_operation_number(input("Select operations form 1, 2, 3, 4 :"))

if select_operation_type > 0:

    number_1 = is_number(input("Enter first number: "))
    number_2 = is_number(input("Enter second number: "))

    if select_operation_type == 1:
        print(number_1, "+", number_2, "=",
                        add(number_1, number_2))

    elif select_operation_type == 2:
        print(number_1, "-", number_2, "=",
                        subtract(number_1, number_2))

    elif select_operation_type == 3:
        print(number_1, "*", number_2, "=",
                        multiply(number_1, number_2))

    elif select_operation_type == 4:
        print(number_1, "/", number_2, "=",
                        divide(number_1, number_2))
        
else: print('Bad Operation type')
