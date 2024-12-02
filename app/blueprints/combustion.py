from flask import Blueprint, request, jsonify, make_response
from app.services.combustion_service import combustion_calc, combustion_county, comobustion_convert_mass_kg

combustion_bp = Blueprint('combustion_bp', __name__)

@combustion_bp.route('/combustion/calc', methods=['POST'])
def combustion_calc():
    """
    Takes in a feedstock amount in mass flow rate with a specified unit, with a waste type of either (i) sludge, (ii) food, (iii) fog, (iv) green or (v) manure
    """
    None
    
@combustion_bp.route('/combustion/county', methods=['GET'])
def combustion_county():
    None