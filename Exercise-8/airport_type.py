# Write a program that asks the user to enter the area code (for example FI) and prints out the airports located in that country ordered by airport type. For example,
# Finland has 65 small airports, 15 helicopter airports and so on.

import mariadb

connection = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Database@26',
         autocommit=True
         )

def get_airport_name_by_type(connection, area_code_entered):
    sql = f"SELECT name, type FROM airport WHERE  iso_country = '{area_code_entered}' ORDER BY type"
    cursor=connection.cursor()
    cursor.execute(sql, (area_code_entered,))
    result = cursor.fetchall()
    if result:
        for a in result:
            print(f" airport name: {a[0]}, type: {a[1]}")
    else:
        print(f"no record found : {area_code_entered}")
        cursor.close()

area_code_entered = input("please enter area code: ")
get_airport_name_by_type(connection, area_code_entered)

connection.close()