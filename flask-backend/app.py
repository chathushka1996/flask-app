from flask import Flask
from ping import Ping
from products import Products

app = Flask(__name__)

app.add_url_rule('/ping', view_func=Ping.ping, methods=["GET"])
app.add_url_rule('/api/products/add', view_func=Products.add_product, methods=["POST"])

if __name__ == "__name__":
    app.run('localhost', '5000', debug=True)