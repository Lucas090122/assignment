import mysql.connector

def getEmployeesByLastName(last_name):
    sql = "SELECT * FROM AIRPORT LIMIT 10"
    print(sql)
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount >0 :
        for row in result:
            print(f"Hello! I'm {row[2]} {row[1]}. My salary is {row[3]} euros per month.")
    return

# Main program
connection = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='root',
         password='12121122',
         autocommit=True
         )

last_name = input("Enter last name: ")
getEmployeesByLastName(last_name)
