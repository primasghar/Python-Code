# 1. Write a function that returns a random dice roll between 1 and 6. The function should not have any parameters. Write
# a main program that rolls the dice until the result is 6. The main program should print out the result of each roll.
import random

# def roll_dice():
#     return random.randint(1,6)
#
# result = 0
#
# while result != 6:
#     result = roll_dice()
#     print(result)

# ----------------------------------------------------------------------------------------------------------------------
# 2. Modify the function above so that it gets the number of sides on the dice as a parameter. With the modified function
# you can for example roll a 21-sided role-playing dice. The difference to the last exercise is that the dice rolling
# in the main program continues until the program gets the maximum number on the dice, which is asked from the user at
# the beginning.

# max_sides = int(input("Enter maximum number of you want for a dice: "))
#
# def roll_dice(sides):
#     return random.randint(1, sides)
#
# result = 0
#
# while result != max_sides:
#     result = roll_dice(max_sides)
#     print(result)

# ----------------------------------------------------------------------------------------------------------------------
# 3. Write a function that gets the quantity of gasoline in American gallons and returns the number converted to liters.
# Write a main program that asks for a volume in gallons from the user and converts the value to liters. The conversion
# must be done by using the function. Conversions continue until the user inputs a negative value.

# print("Convert Gallons to Liters\n")
#
# def gallons_to_liters(gallons):
#     return gallons * 3.785
#
#
# volume_in_gallons = float(input("Enter gasoline quantity in gallons: \n"))
#
# while volume_in_gallons > 0:
#     liters = gallons_to_liters(volume_in_gallons)
#     print(f"{volume_in_gallons} gal of gasoline is equal to {liters} L. \n" )
#     volume_in_gallons = float(input("Enter gasoline quantity in gallons: \n"))


# ----------------------------------------------------------------------------------------------------------------------
# 4. Write a function that gets a list of integers as a parameter. The function returns the sum of all the numbers in the
# list. For testing, write a main program where you create a list, call the function, and print out the value it returned.


# def sum_it_up(list_of_integers):
#     result = 0
#     for i in list_of_integers:
#         result = i + result
#     return result
#
#
# num_list = []
#
#
# while True:
#     try:
#         enter_integer = int(input("Please enter a number: "))
#         num_list.append(enter_integer)
#
#     except ValueError:
#         print(sum_it_up(num_list))
#         break

# ----------------------------------------------------------------------------------------------------------------------
# 5. Write a function that gets a list of integers as a parameter. The function returns a second list that is otherwise the
# same as the original list except that all uneven numbers have been removed. For testing, write a main program where you
# create a list, call the function, and then print out both the original as well as the cut-down list.

def even_list_fn(list_of_integers):
    even_list = []
    for i in list_of_integers:
        if i % 2 == 0:
            even_list.append(i)
    return even_list


original_list = []

while True:
    try:
        user_entered_int = int(input("Please enter a number: "))
        original_list.append(user_entered_int)

    except ValueError:
        print("You have exited the program")
        print(f"The original list is: {original_list} \nThe even list is:{even_list_fn(original_list)}")
        break









# ----------------------------------------------------------------------------------------------------------------------
# 6. Write a function that receives two parameters: the diameter of a round pizza in centimeters and the price of the pizza
# in euros. The function calculates and returns the unit price of the pizza per square meter. The main program asks the
# user to enter the diameter and price of two pizzas and tells the user which pizza provides better value for money
# (which of them has a lower unit price). You must use the function you wrote for calculating the unit prices.