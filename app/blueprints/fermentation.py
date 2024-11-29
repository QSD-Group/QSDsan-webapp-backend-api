from flask import Blueprint, request, jsonify, make_response
from app.services.fermentation_service import fermentation_calc, fermentation_county, fermentation_convert_mass_kg

fermentation_bp = Blueprint('fermentation_bp', __name__)

@fermentation_bp.route('/fermentation/calc', methods=['POST'])
def fermentation_calc():
    None
    
@fermentation_bp.route('/fermentation/county', methods=['GET'])
def fermentation_county():
    None
    
