from flask import Flask, jsonify, request,abort
app = Flask(__name__)
from base.product_records import ProductsPoints
from base.sales_records import Transactions

products_list=[]
sale_orders=[]

#admin can get all products
@app.route('/api/v1/products/', methods=['GET']) 
def get_all_products():
    
    return jsonify(products_list), 200

#admin can add a product
@app.route('/api/v1/products/', methods = ['POST'])
def post_product():
    data = request.get_json()
    product = {
      "product_id" : data['product_id'],
      "product_name": data['product_name'],
      "product_price": data['product_price']
    }
    products_list.append(product)
    return jsonify ({"message": "product added"})

#admin/store attendant can get a specific product
@app.route("/api/v1/products/<product_id>", methods=['GET'])
def get_specific_product(product_id):
 
    if product in products_list if ["product_id" ] == product_id]
       return jsonify({"product": product})

 else:
    return ({"message": "product not found"})
    

@app.route('/api/v1/sales/',methods = ['POST'])
def add_sale_order():
    trades = request.get_json()     
    sale_id = trades['sale_id']
    sale_product = trades['sale_product']
    sale_total = trades['sale_total']    
    sale_orders.append(Transactions(sale_id,sale_product,sale_total))
    return jsonify({"message": "sales added"}),200

#admin can get all sale order records
@app.route('/api/v1/sales/', methods =['GET'])
def get_all_sales():
    reply =[]
    for sale_order in sale_orders:
        reply.append(sale_order.return_sales_records())
    return jsonify(reply)


if __name__== '__main__':
 app.run(debug = True)

