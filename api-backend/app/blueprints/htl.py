from flask import Blueprint, request, jsonify, make_response
from app.services.htl_service import htl_calc, htl_county, htl_convert_sludge_mass_kg

htl_bp = Blueprint('htl_bp', __name__)

@htl_bp.route('/htl/calc', methods=['POST'])
def htl_calc():
    None
    
@htl_bp.route('/htl/county', methods=['GET'])
def htl_county():
    None