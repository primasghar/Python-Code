import mariadb

print(mariadb.__version__)

connection = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Database@26',
         autocommit=True
         )

def get_airport_name_location(connection, icao_code_entered):
    sql = f"SELECT name, municipality FROM airport WHERE ident = '{icao_code_entered}'"
    cursor=connection.cursor()
    cursor.execute(sql, (icao_code_entered,))
    result = cursor.fetchall()
    if result:
        for a in result:
            print(f" airport name: {a[0]}, town: {a[1]}")
    else:
        print(f"no record found : {icao_code_entered}")
        cursor.close()

icao_code_entered = input("please enter ICAO code of an airport: ")
get_airport_name_location(connection, icao_code_entered)

connection.close()