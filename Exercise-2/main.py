import random

# 1. Write a program that asks your name and then greets you by your name:

print("Hello, " + input("What is your name? ") + "!.")


# -----------------------------------------------------------------------------------------------------------------
# 2. Write a program that asks the user for the radius of a circle and the prints out the area of the circle.

radius = int(input("What is the radius of a circle? "))
area = 3.14 * (radius**2)
print(f"The area of a circle is {area}")


# -----------------------------------------------------------------------------------------------------------------
# 3. Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle.
# The perimeter of a rectangle is the sum of the lengths of each four sides.

rectangle_length = int(input("What is the length of a rectangle? "))
rectangle_width = int(input("What is the width of a rectangle? "))

rectangle_perimeter =  2 * (rectangle_length + rectangle_width)
rectangle_area = rectangle_length * rectangle_width

print(f"The Perimeter of the rectangle is: {rectangle_perimeter} and the Area of the rectangle is: {rectangle_area}")


# -----------------------------------------------------------------------------------------------------------------
# 4. Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers.

Integer_1 = int(input("Please enter the first integer of your choice "))
Integer_2  = int(input("Please enter the second integer of your choice "))
Integer_3  = int(input("Please enter the third integer of your choice "))

sum_of_three_integers = Integer_1 + Integer_2 + Integer_3
product_of_three_integers = Integer_1 * Integer_2 * Integer_3
average_of_three_integers = sum_of_three_integers / 3

print(f"The sum of three integers is: {sum_of_three_integers}.\nThe product of three integers is: {product_of_three_integers}.\nThe average of three integers is: {average_of_three_integers}.")


# -----------------------------------------------------------------------------------------------------------------
# 5. Write a program that asks the user to enter a mass in medieval units: talents (leiviskä), pounds (naula), and lots (luoti).
# The program converts the input to full kilograms and grams and outputs the result to the user:

# One talent is 20 pounds.
# One pound is 32 lots.
# One lot is 13,3 grams.

# Convert talents to kg and g

print("Convert talents to kilogram and grams.")
user_talents = int(input("Enter talents "))

one_talent_in_grams = 20 * 32 * 13.3

talent_to_g = round( user_talents * one_talent_in_grams)
talent_to_kg = round(talent_to_g/1000)

print(f"{ user_talents} talents = {talent_to_kg} kilograms or {talent_to_g} grams.")


# Converting pounds to kg and g

print("Convert pounds to kilogram and grams.")
user_pounds = int(input("Enter pounds "))

one_pounds_in_grams = 32 * 13.3

pounds_to_g = round(user_pounds * one_pounds_in_grams, 2)
pounds_to_kg = round(pounds_to_g/1000 , 2)

print(f"{user_pounds} pounds = {pounds_to_kg} kilograms or {pounds_to_g} grams.")

# Converting lots to kg and g

print("Convert lots to kilogram and grams.")
user_lots = int(input("Enter pounds "))

lots_to_g = round(user_lots * 13.3, 2)
lots_to_kg = round(lots_to_g/1000, 2)

print(f"{user_lots} lots = {lots_to_kg} kilograms or {lots_to_g} grams.")


# -----------------------------------------------------------------------------------------------------------------
# 6. Write a program that draws two random combinations of numbers for a combination lock:
# a 3-digit code where each number is between 0 and 9.
# a 4-digit code where each number is between 1 and 6.


print("Three digit code")

digit1 = str(random.randint(0,9))
digit2 = str(random.randint(0,9))
digit3 = str(random.randint(0,9))

print(f"{digit1}{digit2}{digit3}\n")



print("Four digit code")

digit_1 = str(random.randint(0,6))
digit_2 = str(random.randint(0,6))
digit_3 = str(random.randint(0,6))
digit_4 = str(random.randint(0,6))

print(f"{digit_1}{digit_2}{digit_3}{digit_4}")

