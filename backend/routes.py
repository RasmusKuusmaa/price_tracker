from flask import Blueprint, request, jsonify
from models import db, Product

track_product = Blueprint('track_product', __name__)  

@track_product.route('/track', methods=['POST'])
def track():
    data = request.get_json()
    print("Received data:", data) 


    required_keys = ['url', 'original_price', 'email']
    for key in required_keys:
        if key not in data:
            return jsonify({"error": f"Missing key: {key}"}),
    
    try:
        cur_price = data.get('cur_price')  #

        product = Product(
            url=data['url'],
            original_price=data['original_price'],
            cur_price=cur_price,
            email=data['email']
        )
        
        db.session.add(product)
        db.session.commit()

        return jsonify({"message": "Product saved"}), 201
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500
