import os
import pymysql
from flask import jsonify
import datetime

user = os.environ.get('CLOUD_SQL_USERNAME')
password = os.environ.get('CLOUD_SQL_PASSWORD')
db_name = os.environ.get('CLOUD_SQL_DATABASE_NAME')
connection_name = os.environ.get('CLOURD_SQL_CONNECTION_NAME')

def open_connection():
    # if deployed via google app engine (gae_env = standard when deployed)
    if os.environ.get('GAE_ENV') == 'standard':
        unix_socket = '/cloudsql/%s' % (connection_name)
        connection = pymysql.connect(user=user, password=password, unix_socket=unix_socket, db_name=db_name)

    # if running locally    
    else:
        host = '127.0.0.1'
        connection = pymysql.connect(user=user, password=password, host=host, db=db_name)


def create_order(order_request_details):
    customer_id = order_request_details["id"]
    delivery_address = order_request_details["address"] + order_request_details["postcode"]
    product_id = order_request_details["product_id"]
    status = "Processing"
    track_point = "Warehouse - Bournemouth"
    estimated_delivery = datetime.date.isoformat(datetime.date.today() + datetime.timedelta(days=+7)) # 7 days after current date in YYYY-MM_DD
    query = 'INSERT INTO orders(status, product_id, delivery_address, estimated_delivery, track_point, customer_id) ' \
            'VALUES(%s, %s, %s, %s, %s, %s)' % (status, product_id, delivery_address, estimated_delivery, track_point, customer_id)

    connection = open_connection()
    with connection.cursor() as cursor:
        cursor.execute(query)
        cursor.commit()
    connection.close()

