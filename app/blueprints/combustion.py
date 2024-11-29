from flask import Blueprint, request, jsonify, make_response
from app.services.combustion_service import combustion_calc, combustion_county, comobustion_convert_mass_kg

combustion_bp = Blueprint('combustion_bp', __name__)

@combustion_bp.route('/combustion/calc', methods=['POST'])
def htl_calc():
    None
    
@combustion_bp.route('/combustion/county', methods=['GET'])
def htl_county():
    None