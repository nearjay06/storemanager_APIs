from flask import Flask, jsonify, request,abort
app = Flask(__name__)
from model.product_records import ProductsPoints
from model.sales_records import Transactions

products_list=[]
sale_orders=[]

#admin can get all products
@app.route('/api/v1/products/', methods=['GET']) 
def get_all_products():
    if products_list == []:
        return jsonify ({"message":"no products available"}),400
        
    return jsonify(products_list), 200
    
#admin can add a product
@app.route('/api/v1/products/', methods = ['POST'])
def post_product():
    data = request.get_json()
    product = {
      "product_id" :len(products_list)+1,
      "product_name": data['product_name'],
      "product_price": data['product_price']
    }
    if "product_name" in product == 0:
        return ({"message":"invalid inputs"}),400

    products_list.append(product)
    return jsonify ({"message": "product added"})


#admin/store attendant can get a specific product
@app.route("/api/v1/products/<product_id>", methods=['GET'])
def get_specific_product(product_id):
    try:
        if len(products_list) != 0:
            products = [product for product in products_list if product["product_id"]==product_id]
            return jsonify({"message": products[0]})
        else:
            return jsonify({"message":"you  dont have product in the list yet"}),200
    except Exception as e:
        print(e)
        return jsonify({"message":"you  dont have product in the list yet"}),200

    
@app.route('/api/v1/sales/',methods = ['POST'])
def add_sale_order():
    
    trades = request.get_json() 
    sales ={    
            "sale_id":trades["sale_id"],
            "sale_product":trades["sale_product"],
            "sale_total" :trades["sale_total"]
        }   
    if sales == 0:
        return jsonify({"message":"no input for sales"}),400
    sale_orders.append(sales)
    return jsonify({"message": "sale order record created"}), 201
     
 #admin can get all sale order records
@app.route('/api/v1/sales/', methods =['GET'])
def get_all_sales():
    if sale_orders == []:
         return jsonify ({"message":"no sale records available"}),400

    return jsonify({"message":sale_orders}),200

#admin/store attendant can get a specific sale order record
@app.route("/api/v1/sales/<sale_id>", methods=['GET'])
def get_specific_sale_order_record(sale_id):
    for sale_id in sale_orders:
        
         return jsonify ({'sale_orders': sale_id}),200

    sale_orders.append(sale_orders)
    return jsonify({"message": "sale order record not found"}),400
         
    
if __name__== '__main__':
 app.run(debug = True)

