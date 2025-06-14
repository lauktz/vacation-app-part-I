from flask import Blueprint, request
from controllers.like_controller import LikeController

like_bp = Blueprint('likes', __name__)

@like_bp.route('/likes', methods=['POST'])
def add_like():
    data = request.get_json()
    return LikeController.add_like(data)

@like_bp.route('/likes', methods=['DELETE'])
def remove_like():
    data = request.get_json()
    return LikeController.remove_like(data)

@like_bp.route('/likes/<int:user_id>', methods=['GET'])
def get_likes_by_user(user_id):
    return LikeController.get_likes_by_user(user_id)