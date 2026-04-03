import mariadb

connection = mariadb.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='Database@26',
         autocommit=True
         )


def fetch_airport_info_query(icao):
    sql = f"SELECT name, municipality FROM airport WHERE ident = %s"
    # print(sql)
    cursor = connection.cursor()
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result
