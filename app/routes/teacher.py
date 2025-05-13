from flask import Blueprint

bp = Blueprint('teacher', __name__, url_prefix='/teacher')

@bp.route('/test', methods=['GET'])
def test_teacher():
    return {'msg': 'Teacher route works!'}
