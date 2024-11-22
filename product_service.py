from fastapi import FastAPI

app = FastAPI()

# Sample product data
products = [
    {"id": 1, "name": "Laptop", "price": 1000},
    {"id": 2, "name": "Smartphone", "price": 500},
    {"id": 3, "name": "Tablet", "price": 300},
]

@app.get("/products")
def get_products():
    """Retrieve a list of products."""
    return {"products": products}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    """Retrieve details of a specific product."""
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return product
    return {"error": "Product not found"}, 404

 ["python", "app.py"]



app = Flask(__name__)

@app.route('/products', methods=['GET'])
def get_products():
    products = [
        {"id": 1, "name": "Product 1", "price": 100},
        {"id": 2, "name": "Product 2", "price": 150},
        {"id": 3, "name": "Product 3", "price": 200}
    ]
    return jsonify(products)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
