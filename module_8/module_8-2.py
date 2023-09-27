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
iso_country = input("Please enter the country code:")
sql = f"select type, count(*) from airport where iso_country = '{iso_country}' group by type;"
country = f"select name from country where iso_country = '{iso_country}';"
cursor = connection.cursor()
cursor.execute(sql)
result = cursor.fetchall()
cursor_country = connection.cursor()
cursor.execute(country)
country_name = cursor.fetchall()
i = ','.join([f' {item[1]} {item[0]}' for item in result])
print(f"{country_name[0][0]} has{i} airports.")