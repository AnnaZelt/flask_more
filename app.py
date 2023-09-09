import json
from flask import Flask, render_template, request

app = Flask(__name__)

products = [
    {'name':'apple'
    ,'price':4,
    'stock':10},
    {'name':'banana'
    ,'price':5,
    'stock':9},
    {'name':'carrot'
    ,'price':6,
    'stock':8}
    ]
total = 0
reset = False

def save_cart_to_file(cart):
    with open('cart.json', 'w') as json_file:
        json.dump(cart, json_file)

def load_cart_from_file():
    try:
        with open('cart.json', 'r') as json_file:
            cart = json.load(json_file)
    except FileNotFoundError:
        cart = []  # Create an empty cart if the file doesn't exist
    return cart

cart = load_cart_from_file()

@app.route("/")
def index():
    global total, products, cart, reset
    try:
        selection = request.args.get('selection')
        
        if selection is not None:
            selected = int(selection)

            if 0 <= selected < len(products) and products[selected]['stock'] > 0:
                # Decrease stock in products and increase stock in cart
                products[selected]['stock'] -= 1

                # Check if the product is already in the cart
                cart_product = next((item for item in cart if item['name'] == products[selected]['name']), None)

                if cart_product:
                    # If the product is in the cart, increase its stock by 1
                    cart_product['stock'] += 1
                else:
                    # If the product is not in the cart, add it with stock 1
                    cart_product = dict(products[selected])
                    cart_product['stock'] = 1
                    cart.append(cart_product)

                tmp_total = cart_product['price']
                total += tmp_total

    except (ValueError, IndexError):
        pass
    save_cart_to_file(cart)
    reset = bool(request.args.get('reset'))
    if reset:
        reset_cart = []
        save_cart_to_file(reset_cart)
        cart = load_cart_from_file()
        reset = False   
    return render_template("index.html", products=products, cart=cart, total=total, reset=reset)

@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")


