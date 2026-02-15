import mariadb
from geopy import distance

# Write a program that asks the user to enter the ICAO codes of two airports.
# The program prints out the distance between the two airports in kilometers.
# The calculation is based on the airport coordinates fetched from the database.
# Calculate the distance using the geopy library: https://geopy.readthedocs.io/en/stable/.
# Install the library by selecting View / Tool Windows / Python Packages in your PyCharm IDE,
#write geopy into the search field and finish the installation.

connection = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Database@26',
         autocommit=True
         )

def get_distance_between_airports(connection, airport_A_ICAO, airport_B_ICAO):
    sql = f"SELECT name, latitude_deg, longitude_deg FROM airport WHERE ident = '{airport_A_ICAO}' or ident = '{airport_B_ICAO}'"
    cursor=connection.cursor()
    cursor.execute(sql, (airport_A_ICAO, airport_B_ICAO))
    result = cursor.fetchall()
    if result:
        a = result[0]
        b = result[1]
        
        p1 = (a[1], a[2])
        p2 = (b[1], b[2])

        flat_distance = distance.distance(p1[:2], p2[:2]).km

        print(f"The distance between {a[0]} and {b[0]} is {flat_distance:2f} km")

    else:
        print(f"no record found : {airport_A_ICAO} or {airport_B_ICAO}")
        cursor.close()

airport_A_ICAO = input("please enter ICAO code for airport A: ")
airport_B_ICAO = input("please enter ICAO code for airport B: ")

get_distance_between_airports(connection, airport_A_ICAO, airport_B_ICAO)

connection.close()