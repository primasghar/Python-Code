

# 1. Write a program that asks the user how many dice to roll. The program rolls all the dice once and prints out the sum
# of the numbers. Use a for loop.
# import random

# print("Dice roll")
#
# number_of_dice = int(input("Enter the number of dice you want to roll: "))
#
# dice=0
# result=0
#
# for i in range(number_of_dice):
#     dice=dice+1
#     num_output = random.randint(1,6+1)
#     print(f"{dice}-{num_output}")
#     result += num_output
#
# print(f"The result is {result}")

# ----------------------------------------------------------------------------------------------------------------------
# 2. Write a program that asks the user to enter numbers until they input an empty string to quit. At the end, the program
# prints out the five greatest numbers sorted in descending order. Hint: You can reverse the order of sorted list items
# by using the sort method with the reverse=True argument.

# print("Five greatest numbers\n(Please enter minimum 5 numbers to get the result)")
#
# number_list = []
#
# while True:
#     try:
#         number = int(input("Enter the number: "))
#         number_list.append(number)
#     except ValueError:
#         break
#
# number_list.sort(reverse=True)
#
# index_range = 5
#
# if len(number_list) >= index_range:
#     for i in range(index_range):
#             print(number_list[i])
# else:
#     print("You need minimum of 5 integer input values to get the result")

# ----------------------------------------------------------------------------------------------------------------------
# 3. Write a program that asks the user for an integer and tells if the number is a prime number. Prime numbers are number
# that are only divisible by one or the number itself.

# print("Find out if the number is a Prime number")
#
# user_number= int(input("Enter the number: "))
#
# list_of_factors = []
#
# for i in range(1, user_number+1):
#     print(i)
#     if user_number % i == 0:
#         list_of_factors.append(i)
#         print(list_of_factors)
#
# if len(list_of_factors) == 2 and list_of_factors[0] == 1 and list_of_factors[1] == user_number:
#     print("The number is a Prime number")
# else:
#     print("The number is not a Prime number")

# ----------------------------------------------------------------------------------------------------------------------
# 4. Write a program that asks the user to enter the names of five cities one by on (use a for loop for reading the names)
# and stores them into a list structure. Finally, the program prints out the names of the cities one by one, one city
# per line, in the same order they were read as input. Use a for loop for asking the names and a for/in loop to iterate
# through the list.


print("Five cities")

city_name_list = []

for x in range(5):
    user_entered_city = input("Enter a city: ")

    if user_entered_city in city_name_list:
        print("This city name already exists. Please enter a new city name.")
        user_entered_city = input("Enter a city: ")

    city_name_list.append(user_entered_city)

for city_name in city_name_list:
    print(city_name)
















