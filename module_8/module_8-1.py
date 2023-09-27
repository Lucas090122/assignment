import mysql.connector


# main program
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='12121122',
         autocommit=True
         )
icao = input("Please enter the ICAO code of your airport:")
sql = f"select name, municipality from airport where ident = '{icao}'"
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()
if cursor.rowcount > 0:
    for row in result:
        print(f"For ICAO code {icao}, the airport name is {row[0]}, location at {row[1]}")
else:
    print("Unexist ICAO code.")