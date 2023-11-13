from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/home')
def home_page():
    return render_template("home.html")  # connecting html to flask


@app.route('/market')
def market_page():
    items = [
        {"id": 1, "name": "Phone", "barcode": "87700655", "price": 500},
        {"id": 2, "name": "laptop", "barcode": "84700655", "price": 700},
        {"id": 3, "name": "keyboard", "barcode": "487700655", "price": 800}
    ]
    return render_template("market.html", item_name=items)

# @app.route('/about/<username>')  dynamic routes
# def about_page(username):
#     return  f"<h1>About Page of {username}</h1>"
