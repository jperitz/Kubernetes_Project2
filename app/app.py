from flask import Flask
from typing import List, Dict
import mysql.connector
import json

app = Flask(__name__)

def fav_colors() -> List[Dict]:
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
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

@app.route('/')
def index() -> str:
    return json.dumps({'fav_colors': fav_colors()})

if __name__ == '__main__':
    app.run(host='0.0.0.0')

