from flask import Blueprint, request, jsonify
from models import db, Product
from flask_cors import CORS
from scraper import get_price
track_product = Blueprint('track_product', __name__)  
CORS(track_product)
@track_product.route('/track', methods=['POST'])
def track():
    data = request.get_json()
    print("Received data:", data) 

    required_keys = ['url','email']
    for key in required_keys:
        if key not in data:
            return jsonify({"error": f"Missing key: {key}"}), 400  

    try:
        price = (get_price(data['url']))
        price = price.replace('\xa0', '').replace('€', '')
        original_price = cur_price = price

        product = Product(
            url=data['url'],
            original_price=original_price,
            cur_price=cur_price,
            email=data['email']
        )
        
        db.session.add(product)
        db.session.commit()

        return jsonify({"message": "Product saved"}), 201  
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500 

@track_product.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    print('received data: ', data)

    return jsonify({"message": "success"}), 200
