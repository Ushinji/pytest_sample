from flask import jsonify, request
from app import application


@application.route("/sum", methods=["GET"])
def get_sum():
    a = request.args.get('a')
    b = request.args.get('b')

    if a.isdigit() and b.isdigit():
        return jsonify({'result': int(a) + int(b)})
    else:
        return jsonify({
            'errors': f'Query params must be integer. a: {a}, b: {b}'
        }), 422
