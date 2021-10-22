from flask import Flask
from routes import classifier_bp
from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(classifier_bp, url_prefix='/')
CORS(app)

app.run(debug=True)
