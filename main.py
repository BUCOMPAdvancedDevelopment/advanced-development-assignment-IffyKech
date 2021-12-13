import logging
import requests
from flask import Flask, render_template, request, redirect, url_for
from db_scripts import create_order

app = Flask(__name__)

def get_google_function_data(url):
    request = requests.get(url)
    data = request.json()
    return data

@app.route('/')
def login_redirect():
    return redirect(url_for('render_login'))

@app.route('/login')
def render_login():
    return render_template('login.html')

""" USER SECTION """
@app.route('/home')
def render_index():
    return render_template('index.html')

@app.route('/products', methods=["GET"])
def render_products():
    list_products_function_url = "https://europe-west2-ad-lab-21.cloudfunctions.net/list_products"
    products_data = get_google_function_data(list_products_function_url)
    
    return render_template('products.html', products_data=products_data)

@app.route('/product', methods=["GET"])
def render_product():
    product_id = request.args.get('id')
    return_product_function_url = "https://europe-west2-ad-lab-21.cloudfunctions.net/return_product?id=" + product_id
    product_data = get_google_function_data(return_product_function_url)

    return render_template('product.html', product_data=product_data)

@app.route('/order', methods=['POST'])
def create_order():
    order_request_details = request.get_json()
    create_order(order_request_details)
    print("Done")
    return "success", 200

@app.route('/orders')
def render_orders():
    return render_template('orders.html')


"""ADMIN SECTION """
@app.route('/admin')
def render_admin():
    return render_template('admin.html')

""" ERROR HANDLERS """
@app.errorhandler(500)
def server_error(e):
    logging.exception('An error occurred during a request')
    return e, 500

# @app.errorhandler(404)
# def page_not_found(error):
#     return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 8080, debug = True)
    