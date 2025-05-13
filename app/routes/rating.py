from flask import Blueprint

bp = Blueprint('rating', __name__, url_prefix='/rating')

@bp.route('/test', methods=['GET'])
def test_rating():
    return {'msg': 'Rating route works!'}
