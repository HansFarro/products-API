from flask import Flask, jsonify, request

app = Flask(__name__)

from products import products

# GET REQUESTS
@app.route('/ping')
def another():
  return jsonify({"message": "pong"})

@app.route('/products', methods=['GET'])
def getProducts():
  return jsonify({"products": products, "message":"Product's list"})

@app.route('/products/<string:product_name>')
def getProduct(product_name):
  productFound = [product for product in products if product['name'] == product_name]
  if(len(productFound) > 0):
      return jsonify({"product": productFound[0]})
  return jsonify({"product": "Product not found"})

# POST REQUEST
@app.route('/products', methods=['POST'])
def addProduct():
  # print(request.json)
  newProduct = {
    "name": request.json['name'],
    "price": request.json['price'],
    "quantity": request.json['quantity']
  }
  products.append(newProduct)
  return jsonify({"message":"Product added succesfully","products": products[-1]})

# PUT REQUEST
@app.route('/products/<string:product_name>',methods=['PUT'])
def editProduct(product_name):
  productFound = [product for product in products if product['name'] == product_name]
  if(len(productFound)> 0):
    productFound[0]['name'] = request.json['name']
    productFound[0]['price'] = request.json['price']
    productFound[0]['quantity'] = request.json['quantity']
    return jsonify({
      "message":"Product updated",
      "product": productFound[0]
    })
  return jsonify({"message":"Product not found"})
  
if __name__ == '__main__':
  app.run(debug=True, port=4000)