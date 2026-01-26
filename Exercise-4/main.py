# 1- Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.
import random

# number = 1
#
# while number <= 1000:
#     if number % 3 == 0:
#         print(number)
#     number += 1


#-----------------------------------------------------------------------------------------------------------------------
# 2- Write a program that converts inches to centimeters until the user inputs a negative value. Then the program ends.

# an_inch = "2.54cm"
#
# user_input = int(input("Enter an integer to convert from inch to cm: "))
#
# while  not (user_input < 1):
#     input_in_cm = user_input * 2.54
#     print(input_in_cm)
#     user_input = int(input("Enter an integer to convert from inch to cm: "))
#
# print("The program ended")


# 3- Write a program that asks the user to enter numbers until they enter an empty string to quit. Finally, the program
# prints out the smallest and largest number from the numbers it received.

# userInput = input("Enter a number: ")
#
# numbers_list = []
#
# while True:
#     try:
#         value = int(userInput)
#         numbers_list.append(value)
#         # print(numbers_list)
#         userInput = input("Enter a number: ")
#
#     except ValueError:
#         print("Exiting the program")
#         break
#
#
# smallest_no = min(numbers_list)
# largest_no = max(numbers_list)
#
# print(f"The smallest number is {smallest_no} and the largest number is {largest_no}")

#-----------------------------------------------------------------------------------------------------------------------
# 4- Write a game where the computer draws a random integer between 1 and 10. The user tries to guess the number until
# they guess the right number. After each guess the program prints out a text: Too high, Too low or Correct. Notice that
# the computer must not change the number between guesses.

# print("Guess the Number")

# computer_number = random.randint(1, 10)
#
# user_guess = int(input("Please guess the number between 1 to 10: "))
#
# print(computer_number)
#
# while user_guess != computer_number:
#     if user_guess < computer_number:
#         print("Too low")
#     else:
#         print("Too high")
#     user_guess = int(input("Please again guess the number between 1 to 10: "))
#     print(computer_number) #to check computer ans have not changed.
# else:
#     print("Correct")


#-----------------------------------------------------------------------------------------------------------------------
# 5- Write a program that asks the user for a username and password. If either or both are incorrect, the program ask the
# user to enter the username and password again. This continues until the login information is correct or wrong credentials
# have been entered five times. If the information is correct, the program prints out Welcome. After five failed attempts
# the program prints out Access denied. The correct username is python and password rules.


print("Login")

correct_username = "python"
correct_password = "rules"

entered_username = (input("Please enter username "))
entered_password = (input("Please enter password "))

attempts_to_login = 0

while entered_username != correct_username and entered_password != correct_password:
    attempts_to_login += 1
    if attempts_to_login > 5:
        print("Access denied")
        break
    print("The username or password is incorrect. Please try again.")

    user_name = (input("Please enter username "))
    user_password = (input("Please enter password "))
else:
    print("Welcome")






#-----------------------------------------------------------------------------------------------------------------------
# 6- Implement an algorithm for calculating an approximation for the value of pi (π). Let's assume that A is a unit circle.
# A unit circle has the radius of one and it is centered at the origin (0,0). Smallest possible square B is drawn around
# the unit circle so that circle A is completely inside the square. The corners of the square are now (-1,-1), (1, -1), (1, 1),
# and (-1, 1). If a large number of random points are scattered inside the square, the fraction of points that fall inside the
# circle A correlates with the fraction of the area of circle A compared to the area of square B: πr^2/4 = π*1^2/4 = π/4.
# This can be used as a simple method for calculating an approximation of the value of pi: Let's generate a large number of
# random points, such as one million, inside square B. Let N be the total number of random points. Each point inside the
# square is tested for whether it resides inside circle A. Let n be the total number of points that fall inside circle A.
# Now we have n/N≈π/4, and from that we get π≈4n/N. Write a program that asks the user how many random points to generate,
# and then calculates the approximate value of pi using the method explained above. At the end, the program prints out the
# approximation of pi to the user. (Notice that it is easy to test if a point falls inside circle A by testing if it fulfills
# the inequation x^2+y^2<1.).