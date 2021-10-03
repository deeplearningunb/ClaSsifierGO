from flask import Blueprint
from views import index, image_processing

sudoku_bp = Blueprint("",__name__)

sudoku_bp.route('/', methods=['GET'])(index)

sudoku_bp.route('/image', methods=['POST'])(image_processing)
