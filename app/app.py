from flask import Flask, render_template, request, Markup
from typing import List, Dict
import mysql.connector
import json

app = Flask(__name__)

def fav_colors() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        #'host': 'db',
        'host': '172.17.0.3',
        'port': '3306',
        'database': 'colors'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM fav_colors')
    results = [{name: color} for (name, color) in cursor]
    cursor.close()
    connection.close()

    return results

add_entry = ("INSERT INTO fav_colors "
            "(name, color) "
            "VALUES (%s, %s)")

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        name = details['name']
        color = details['color']
        data_entry = (name, color)
        cnx = mysql.connector.connect(user='root', password='root', host='172.17.0.2', port='3306', database='colors')
        cnx.close()
        cnx = mysql.connector.connect(user='root', password='root', host='172.17.0.3', port='3306', database='colors')
        cursor = cnx.cursor()
        cursor.execute(add_entry, data_entry)
        cnx.commit()
        cursor.close()
        cnx.close()
        return 'Success!'
    return render_template('index.html')

@app.route('/chart')
def chart():
    labels = ["January","February","March","April","May","June","July","August"]
    values = [10,9,8,7,6,4,7,8]
    colors = [ "#F7464A", "#46BFBD", "#FDB45C", "#FEDCBA","#ABCDEF", "#DDDDDD", "#ABCABC"  ]
    return render_template('chart.html', set=zip(values, labels, colors))

@app.route('/api/data')
def colors() -> str:
    return json.dumps({'fav_colors': fav_colors()})

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

