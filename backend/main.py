from flask import Flask
from routes import sudoku_bp
from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(sudoku_bp, url_prefix='/')
CORS(app)

app.run(debug=True)
