# Write a program that asks the user for a number of a month and then prints out the corresponding season (spring, summer, autumn, winter).
# Save the seasons as strings into a tuple in your program. We can define each season to last three months, December being the first month of winter.


# Winter lasts from November/ to March/April, while summer peaks in July. Spring (April–May) brings rapid snowmelt, and autumn (September–October)

# print("What is the season in this month?")
#
# seasons = ("spring", "summer", "autumn", "winter")
#
# month_number = int(input("Enter the day number (1-12): "))
#
# if  3 <= month_number <=5:
#     print(f"It is {seasons[0]}")
# elif 6 <= month_number <=8:
#     print(f"It is {seasons[1]}")
# elif 9 <= month_number <=11:
#     print(f"It is {seasons[2]}")
# else:
#     print(f"It is {seasons[3]}")


# ----------------------------------------------------------------------------------------------------------------------
# Write a program that asks the user to enter names until he/she enters an empty string. After each name is read the program either
# prints out New name or Existing name depending on whether the name was entered for the first time. Finally, the program lists out the input
# names one by one, one below another in any order. Use the set data structure to store the names.

# name_set = set()
#
# while True:
#     enter_name = input("Enter name of your choice: ")
#     if enter_name == "":
#         break
#     name_set.add(enter_name)
#
#
# for n in name_set:
#     print(n)

# ----------------------------------------------------------------------------------------------------------------------

# Write a program for fetching and storing airport data.
# The program asks the user if they want to

# # enter a new airport,
# If the user chooses to enter a new airport, the program asks the user to enter the ICAO code
# and name of the airport.

# fetch the information of an existing airport
# If the user chooses to fetch airport information instead, the program asks for the ICAO code of the airport
# and prints out the corresponding name.

# # or quit.
# If the user chooses to quit, the program execution ends.
#
# The user can choose a new option as many times they want until they choose to quit.
# (The ICAO code is an identifier that is unique to each airport. For example, the ICAO
# code of Helsinki-Vantaa Airport is EFHK. You can easily find the ICAO codes of different airports online.)

print("Airports in Finland")

airports_in_finland = {"EFHK": "Helsinki-Vantaa Airport",
                       "EFEK":"Kilpisjärvi",
                       "EFIV": "Ivalo",
                       "EFJO":"Joensuu",
                       "EFYL": "Ylivieska"}



while True:
    choose_option = int(input(
        "To enter new airport info: 1 \nTo fetch airport info: 2 \nTo exit the programme: 3 \nType any one option to proceed. "))

    if choose_option == 1:

        new_airport_code = input("Please enter the ICAO code of the airport: ")
        new_airport_name = input("Please enter the name of the airport: ")

        if new_airport_name not in airports_in_finland and new_airport_code not in airports_in_finland:
            airports_in_finland[new_airport_code] = new_airport_name
        else:
            print("This airport information already exists")

    elif choose_option == 2:

        search_by_ICAO = input("Please enter ICAO code of airport you want to search: ")

        if search_by_ICAO in airports_in_finland:
            print(f"The name of the airport is {airports_in_finland[search_by_ICAO]}.")

    else:
        print("Exiting programme")
        break


# for a in airports_in_finland:
#     print(airports_in_finland[a])
