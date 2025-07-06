from flask import Flask, render_template, url_for, request, jsonify
import json
import qrcode
import os

app = Flask(__name__)

# Load products
with open('products.json', 'r') as f:
    products = json.load(f)

# Domain for deployment
BASE_URL = "https://shashishekharm.pythonanywhere.com"  # Update this with your actual PythonAnywhere username

# QR code generation
qr_folder = os.path.join('static', 'qrcodes')
os.makedirs(qr_folder, exist_ok=True)

for product in products:
    # Use video link if available, otherwise link to product detail page
    video_url = product.get("video_url") or f"{BASE_URL}/product/{product['id']}"
    qr_path = os.path.join(qr_folder, f"{product['id']}.png")
    qr = qrcode.make(video_url)
    qr.save(qr_path)

@app.route('/')
def home():
    return render_template('index.html', products=products)

@app.route('/shop')
def shop():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product(product_id):
    product_item = next((p for p in products if p['id'] == product_id), None)
    if not product_item:
        return "Product not found", 404
    qr_code_url = url_for('static', filename=f"qrcodes/{product_item['id']}.png")
    return render_template('product.html', product=product_item, qr_code=qr_code_url)

@app.route('/cart')
def cart():
    return render_template('cart.html')

@app.route('/contact')
def contact():
    return "<h2>Contact Us (Coming Soon)</h2>"

if __name__ == '__main__':
    app.run(debug=True)
