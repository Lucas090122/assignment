from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)


@app.route('/airport/<ICAO>')
def get_airport(ICAO):
    connection = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='12121122',
        autocommit=True
    )
    sql = f"select name, municipality from airport where ident = '{ICAO}'"
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    answer = {'ICAO': f'{ICAO}', 'Name': f'{result[0][0]}', 'Location': f'{result[0][1]}'}
    return jsonify(answer)


app.run(debug=True)