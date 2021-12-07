import logging
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

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

@app.route('/tracking')
def render_tracking():
    return render_template('tracking.html')

@app.route('/products')
def render_products():
    return render_template('products.html')

@app.route('orders')
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
    return 'An internal error occurred.', 500

@app.errorhandler(404)
def page_not_found(error):
    return render_template('404.html'), 404

if __name__ == "__main__":
    app.run(host = "127.0.0.1", port = 8080, debug = True)
    