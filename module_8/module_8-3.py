from geopy import distance
import mysql.connector


def position(icao):
    sql = f"select latitude_deg, longitude_deg from airport where ident = '{icao}';"
    cursor = connection.cursor(dictionary=True)
    cursor.execute(sql)
    result = cursor.fetchall()
    return result


def calculate_distance(airport_1, airport_2):
    start = position(airport_1)
    end = position(airport_2)
    return distance.distance((start[0]['latitude_deg'], start[0]['longitude_deg']), (end[0]['latitude_deg'], end[0]['longitude_deg'])).km



# main program
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='12121122',
         autocommit=True
         )

icao_1 = input("Please enter ICAO code of first airport:")
icao_2 = input("Please enter ICAO code of second airport:")
distance_of_airports = calculate_distance(icao_1, icao_2)
print(f"The distance between these two airports is {distance_of_airports} km.")