from flask import Blueprint, request, jsonify
from models import db, Product

track_product = Blueprint('track_product', __name__)  

@track_product.route('/track', methods=['POST'])
def track():
    data = request.get_json()
    product = Product(url=data['url'], original_price=data['original_price'], 
                    cur_price=data['cur_price'], email=data['email'])
    db.session.add(product)
    db.session.commit()
    return jsonify({"message": "product saved"}), 201
    