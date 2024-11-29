from flask import Blueprint, request, jsonify, make_response # Flask Version 3.0.3
from app.services.htl_service import htl_calc, htl_county, htl_convert_sludge_mass_kg

htl_bp = Blueprint('htl_bp', __name__)

@htl_bp.route('/htl/calc', methods=['POST'])
def htl_calc_data():
    
    sludge = request.args.get('sludge', None)
    
    if sludge is None:
        return make_response(
            jsonify({"error": "Sludge not provided"}), 400 # Bad request, no sludge
        )
    
    unit = request.args.get('unit', 'kghr')
    
    try:
        sludge = float(sludge)
    except ValueError:
        return make_response(
            jsonify({"error": "Sludge should be a number"}), 400 # Bad request, non-float sludge
        )
    
    kg_hr = htl_convert_sludge_mass_kg(sludge, unit)
    
    try:
        result = htl_calc(sludge)
    except TypeError as e:
        return make_response(
            jsonify({"error": str(e)}), 400 # Bad request, non-float sludge
        )
        
    if result:
        price, gwp = htl_calc(kg_hr)
        response_data = {
            "sludge": kg_hr, # In kg/hr
            "price": price, # In $/gallon
            "gwp": gwp # In lb CO2e/gallon
        }
        return make_response(
            jsonify(response_data), 200 # Returns a success status code
        )
    
    return make_response(
        jsonify({"error": "Unexpected error"}), 500 # Unknown error
    )

    
@htl_bp.route('/htl/county', methods=['GET'])
def htl_county_data():
    """
    Takes in a county name and returns the HTL conversion efficiency for that county.
    
    URL Format - GET /htl/county?county_name=county_name
    ---
    tags:
      - HTL
    parameters:
      - name: county_name
        in: query
        type: string
        required: true
        description: 'The name of the county'
        example: 'Atlantic'
      - name: unit
        in: query
        type: string
        required: false
        description: The unit of the sludge mass
        example: 'kghr, tons, tonnes, mgd, m3d'
    responses:
      200:
        description: A successful response
        content:
          application/json:
            schema:
              type: object
              properties:
                county_name:
                  type: string
                  example: 'Atlantic'
                sludge:
                  type: float
                  example: 0.0
                price:
                  type: float
                  example: 0.0
                gwp:
                  type: float
                  example: 0.0
      400:
        description: Bad request
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: 'Bad request'
      404:
        description: Not found
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "County not found"
      500:
        description: Unexpected error
        content:
          application/json:
            schema:
              type: object
              properties:
                message:
                  type: string
                  example: "Unexpected error"
    """
    
    county_name = request.args.get('county_name', None)
    
    if not county_name:
        return make_response(
            jsonify({"message": "County name not provided"}), 400
        )
    
    try:
        result = htl_county(county_name)
    except ValueError:
        return make_response(
            jsonify({"message": "County not found"}), 404
        )
    except TypeError as e:
        return make_response(
            jsonify({"message": str(e)}), 400
        )
    
    if result:
        name, sludge, price, gwp = result
        response_data = {
            "county_name": name,
            "sludge": sludge,
            "price": price,
            "gwp": gwp
        }
        return make_response(
            jsonify(response_data), 200
        )
        
    return make_response(
        jsonify({"message": "Unexpected error"}), 500
    )