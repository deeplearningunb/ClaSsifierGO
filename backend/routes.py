from flask import Blueprint
from views import index, image_processing

classifier_bp = Blueprint("", __name__)

classifier_bp.route('/', methods=['GET'])(index)

classifier_bp.route('/image', methods=['POST'])(image_processing)
