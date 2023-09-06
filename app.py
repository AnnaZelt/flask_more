from flask import Flask, render_template, request

app = Flask(__name__)

# products = [
#     {'name':'apple'
#     ,'price':4,
#     'stock':10},
#     {'name':'banana'
#     ,'price':5,
#     'stock':9},
#     {'name':'carrot'
#     ,'price':6,
#     'stock':8}
#     ]
# cart = []
# tmp_product = []
# total = 0

# @app.route("/")
# def products_index():
#     selection = request.args.get('selection')
#     return render_template("index.html", products=products, selection = selection)

# @app.route("/selection")
# def cart_index():
#     global total
#     tmp_total = 0
#     selection = request.args.get('selection')
#     tmp_product.append(products[int(selection)])
#     tmp_product[0]['stock'] = 1
#     cart.append(tmp_product[0])
#     tmp_total = tmp_product[0]['price']
#     total += tmp_total
#     tmp_product.clear()
#     return render_template("selection.html", products=products, cart=cart, selection=int(selection), total = total)
    
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['POST'])
def picture_practice():
    image_link = request.form.get('image_link')
    return f'The user provided image link is: {image_link}'

if __name__ == '__main__':
    app.run(debug=True)
