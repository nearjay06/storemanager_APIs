from flask import Flask, jsonify, request,abort
from model.product_records import ProductsPoints
from model.sales_records import Transactions
app = Flask(__name__)

products_list=[]
sale_orders=[]

#admin can get and post all products
@app.route('/api/v1/products/', methods=['GET', 'POST']) 
def all_products():
    if request.method == 'GET':
        if products_list == []:
            return jsonify ({"message":"no products available"}),400
            
        return jsonify(products_list), 200
    
    elif  request.method =='POST':
        data = request.get_json()
        print(request)
        if "product_name" not in data:
            return jsonify({"message":"product name required"}), 406

        if len(data["product_name"]) < 1:
            return jsonify({"message":"invalid"}), 400

        if "product_price" not in data:
            return jsonify ({"message":"invalid input"}),400

        if type (data["product_price"]) is not int:
            return jsonify ({"message": "error"}),400
        
        product = {
        "product_id" : len(products_list)+1  ,
        "product_name": data['product_name'],
        "product_price": data['product_price']
        }

        products_list.append(product)
        return jsonify({"message": "product added"}),200

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

#admin can add and get sale order records
@app.route('/api/v1/sales/',methods = ['POST','GET'])
def add_sale_order():
    if request.method =='POST':
        trades = request.get_json()

        if "sale_product" not in trades:
            return jsonify({"message":"no input for sales"}),400
        
        if "sale_total" not in trades:
            return jsonify({"message":"invalid"}),400
        
        if type (trades["sale_total"]) is not int:
            return jsonify ({"message": "invalid input"}),400
            
        sales ={    
                "sale_id":trades["sale_id"],
                "sale_product":trades["sale_product"],
                "sale_total" :trades["sale_total"]
            }
        
        
        sale_orders.append(sales)
        return jsonify({"message": "sale order record created"}), 201
        
    elif request.method =='GET':
        if sale_orders == []:
            return jsonify ({"message":"no sale records available"}),400
        else:
            return jsonify({"message":sale_orders}),200

#admin/store attendant can get a specific sale order record
@app.route("/api/v1/sales/<sale_id>", methods=['GET'])
def get_specific_sale_order_record(sale_id):
    for sale_id in sale_orders:
        sale_orders.append(sale_orders)
        return jsonify ({'sale_orders': sale_id}),200

    return jsonify({"message": "sale order record not found"}),400
         
if __name__== '__main__':
      pass

