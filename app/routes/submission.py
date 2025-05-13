from flask import Blueprint

bp = Blueprint('submission', __name__, url_prefix='/submission')

@bp.route('/test', methods=['GET'])
def test_submission():
    return {'msg': 'Submission route works!'}
