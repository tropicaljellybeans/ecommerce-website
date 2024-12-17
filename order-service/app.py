from flask import Flask, jsonify, request
import sqlite3 
import requests

app = Flask(__name__)

# Define a db
DATABASE = './database.db'

# Check if a conneciton exists and xonnect to the db
def create_table():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        c.execute('''
                        CREATE TABLE IF NOT EXISTS orders(
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        product_id INTEGER NOT NULL,
                        order_quantity INT NOT NULL,
                        total_price REAL NOT NULL)
                        ''')

create_table()


# Create a route to get all orders
@app.route("/", methods = ['GET'])
def get_orders():
    with sqlite3.connect(DATABASE) as conn:
        c = conn.cursor()
        orders = c.execute("SELECT * FROM orders")
        return jsonify(orders)
    
# Create a route to post data 
@app.route("/", methods = ['POST'])
def new_order():
    # Get the data from the request
    data = requests.json

    product_id = data['product_id']
    order_qusntity = data['order_quantity'] 
    
if __name__ == "__main__":
    app.run(debug = True)