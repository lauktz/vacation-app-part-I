from flask import Blueprint
from controllers.vacation_controller import VacationController

vacation_bp = Blueprint('vacations', __name__)

@vacation_bp.route('/vacations', methods=['POST'])
def create_vacation():
    return VacationController.create_vacation()

@vacation_bp.route('/vacations', methods=['GET'])
def get_vacations():
    return VacationController.get_vacations()

@vacation_bp.route('/vacations/<int:vacation_id>', methods=['PUT'])
def update_vacation(vacation_id):
    return VacationController.update_vacation(vacation_id)

@vacation_bp.route('/vacations/<int:vacation_id>', methods=['DELETE'])
def delete_vacation(vacation_id):
    return VacationController.delete_vacation(vacation_id)

@vacation_bp.route('/vacations/<int:vacation_id>', methods=['GET'])
def get_vacation_by_id(vacation_id):
    return VacationController.get_vacation_by_id(vacation_id)
