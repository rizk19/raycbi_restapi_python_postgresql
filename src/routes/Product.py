from flask import Blueprint, jsonify, request
# import uuid

# Entities
# from models.entities.GetPostProduct import GetPostProduct
# Models
from models.ProductModel import ProductModel

main = Blueprint('product_blueprint', __name__)

    
@main.route('/<api_name>', methods=['POST'])
def apiManagers(api_name):
    try:
        method_class = None;
        if len(request.json) > 0 and 'APIName' in request.json:
            for name, obj in globals().items():
                if hasattr(obj, request.json['APIName']) and callable(getattr(obj, request.json['APIName'])):
                    method_class = obj.__name__
                    break;

        if method_class is not None:
            parameters = []
            if (request.json is not None and
                len(request.json) != 0 and
                request.json['inputParameterValues'] is not None and
                len(request.json['inputParameterValues']) > 0):
                
                parameters = request.json['inputParameterValues']

            class_obj = globals()[method_class]()
            affected_rows = getattr(class_obj, request.json['APIName'])(parameters)

            if affected_rows != None:
                return jsonify({
                    'success': True,
                    'message': "Success",
                    'data': affected_rows,
                    'response': {
                        "ReturnMessage": "Success get data",
                        "ReturnCode": 1,
                        "ReturnType": 1
                    }}), 200
            else:
                return jsonify({
                    'success': False, 'message': "Error on get by post method",
                    'data': [], 'response': {
                        "ReturnMessage": "Error get data",
                        "ReturnCode": -3,
                        "ReturnType": 3
                    }}), 500
        else:
            return jsonify({
                'success': False, 'message': "Error on get by post method",
                'data': [], 'response': {
                    "ReturnMessage": "Error get data",
                    "ReturnCode": -3,
                    "ReturnType": 3
                }}), 500

    except Exception as ex:
        return jsonify({
            'success': False, 'message': str(ex),
            'data': [], 'response': {
                "ReturnMessage": "Error get data",
                "ReturnCode": -3,
                "ReturnType": 3
            }}), 500;