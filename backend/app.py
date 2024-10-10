from flask import Flask
from models import db
from routes import track_product
from config import Config
from flask_cors import CORS
app = Flask(__name__)
app.config.from_object(Config)
CORS(app, resources={r"/*": {"origins": "*"}}) 


db.init_app(app)
with app.app_context():  
    db.create_all()
app.register_blueprint(track_product)

if __name__=='__main__':
    app.run(debug=True)