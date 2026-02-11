#1. Write a program that asks a fisher the length of a zander in centimeters.
# If the zander does not fulfill the size limit, the program instructs to release the fish back into the lake
# and notifies the user of how many centimeters below the size limit the caught fish was. A zander must be 42 centimeters
# or longer to meet the size limit.
#
# print("Zander's length measurement app")
#
# optimal_length = 42
#
# zander_length = float(input("Enter length of the zander in cm. "))
#
# if zander_length >= optimal_length:
#     print("Great! The zander fulfills the size limit criteria. ")
# else:
#     size_eval = round(optimal_length - zander_length)
#     print(f"Please release the fish back into the lake. It is {size_eval} cm smaller than optimal size required for harvesting. ")

# ---------------------------------------------------------------------------------------------------------------------
#2. Write a program that asks the user to enter the cabin class of a cruise ship and then prints out a written
# description according to the list below. You must use an if/elif/else structure in your solution.

# LUX: upper-deck cabin with a balcony.
# A: above the car deck, equipped with a window.
# B: windowless cabin above the car deck.
# C: windowless cabin below the car deck.
# If the user enters an invalid cabin class, the program outputs an error message Invalid cabin class.


# print("Cabin class app")

# cabin= input("Choose your cabin class: LUX, A, B, or C . ")

# if cabin == "LUX":
#     print("LUX: upper-deck cabin with a balcony.")
# elif cabin == "A":
#     print("A: above the car deck, equipped with a window.")
# elif cabin == "B":
#     print("B: windowless cabin above the car deck.")
# elif cabin == "C":
#     print("windowless cabin below the car deck.")
# else:
#     print("Invalid cabin class.")

# ---------------------------------------------------------------------------------------------------------------------
#3. Write a program that asks for the biological gender and hemoglobin value (g/l).
# The program the notifies the user if the hemoglobin value is low, normal or high.

# A normal hemoglobin value for adult females is between 117-155 g/l.
# A normal hemoglobin value for adult males is between 134-167 g/l.

# print("Haemoglobin app")

# gender = input("Choose your biological gender: Female or Male: ")

# if gender == "Female" or gender == "female"  or gender == "f":
#     hemoglobin_value = int(input("Enter your hemoglobin value (g/l): "))
#     if hemoglobin_value > 155:
#         print("You have high Hb.")
#     elif hemoglobin_value < 117:
#         print("You have low Hb.")
#     else:
#         print("You have normal Hb.")
# elif gender == "Male" or gender == "male" or gender == "m":
#      hemoglobin_value = int(input("Enter your hemoglobin value (g/l): "))
#      if hemoglobin_value > 167:
#          print("You have high Hb.")
#      elif hemoglobin_value < 134:
#          print("You have low Hb.")
#      else:
#          print("You have normal Hb.")
# else:
#     print("Invalid input.")


#4. Write a program that asks the user to enter a year and notifies the user whether the input year is a leap year.
# A year is a leap year if it is divisible by four. However, years divisible by 100 are leap years only if they are also divisible by 400.


# print("Leap year app")

entered_year = int(input("Please enter year: "))

year_divided_4 = entered_year % 4
year_divided_100 = entered_year % 100
year_divided_400 = entered_year % 400

if (year_divided_4 == 0 and year_divided_100 != 0 ) or year_divided_400 == 0:
    print(f"{entered_year} is a leap year")
else:
    print(f"{entered_year} is not a leap year")