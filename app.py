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
cart = []
tmp_product = []
total = 0

@app.route("/")
def index():
    global total
    tmp_total = 0
    try:
        selection = request.args.get('selection')
        selected = int(selection)
        tmp_product.append(products[selected])
    except: return render_template("index.html", products=products, cart=cart, total = total)
    tmp_product[0]['stock'] = 1
    cart.append(tmp_product[0])
    tmp_total = tmp_product[0]['price']
    total += tmp_total
    tmp_product.clear()
    return render_template("index.html", products=products, cart=cart, selection=selected, total = total)