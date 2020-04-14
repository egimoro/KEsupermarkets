from flask import Flask, request, jsonify, make_response, abort



app = Flask(__name__)


supermarkets = [{
                 'name':'acacia',
                 'no_of_items': 7,
                 'total': 780,
                 'food': 'yes',
                 'location': 'kilimani'},
                 {'name':'nakumatt',
                 'no_of_items': 90,
                 'total': 1480,
                 'food': 'no',
                 'location': 'donholm'},
                {'name':'chandarana',
                 'no_of_items': 3,
                 'total': 13005,
                 'food': 'yes',
                 'location': 'likoni'
                  },
                {'name':'tuskys',
                 'no_of_items': 8,
                 'total': 14005,
                 'food': 'no',
                 'location': 'makadara'},
                {'name':'naivas',
                 'no_of_items': 14,
                 'total': 1305,
                 'food': 'yes',
                 'location': 'cbd'},
                {'name':'kamindi',
                 'no_of_items': 53,
                 'total': 17005,
                 'food': 'yes',
                 'location': 'umoja'}] 

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)

@app.route('/', methods=['GET'])
def start():
    return jsonify({'message':'works'})


@app.route('/api/kesupermarkets', methods=['GET'])
def getSupermarkets():
    return jsonify({'Supermarkets':supermarkets})

@app.route('/api/kesupermarkets/<string:name>', methods=['GET'])
def getSupermarket(name):
    supmkt = [supermarket for supermarket in supermarkets if supermarket['name'] == name]
    if len(supmkt) == 0:
        abort(404)

    return jsonify({'Supermarket': supmkt[0]})

@app.route('/api/kesupermarkets', methods=['POST'])
def addSupermarket():
    if not request.json or not 'name' in request.json:
        abort(404)

    supmkt = {
                'name': request.json['name'],
                'no_of_items': request.json['no_of_items'],
                'total': request.json['total'],
                'food': request.json['food'],
                'location': request.json['location']

            }
    supermarkets.append(supmkt)

    return jsonify({'Supermarket': supmkt}), 201

@app.route('/api/kesupermarkets/<string:name>', methods=['PUT'])
def updateSupermarket(name):
    supmkt = [supermarket for supermarket in supermarkets if supermarket['name'] == name]
    if len(supmkt) == 0:
        abort(404)
    
    supmkt[0]['name'] = request.json.get('name', supmkt[0]['name'])
    supmkt[0]['no_of_items'] = request.json.get('no_of_items', supmkt[0]['no_of_items'])
    supmkt[0]['total'] = request.json.get('total', supmkt[0]['total'])
    supmkt[0]['food'] = request.json.get('food', supmkt[0]['food'])
    supmkt[0]['location'] = request.json.get('location', supmkt[0]['location'])

    return jsonify({'Supermarket': supmkt[0]})

@app.route('/api/kesupermarkets/<string:name>', methods=['DELETE'])
def deleteSupermarket(name):
    supmkt = [supermarket for supermarket in supermarkets if supermarket['name'] == name]
    if len(supmkt) == 0:
        abort(404)
    
    supermarkets.remove(supmkt[0])

    return jsonify({'result': True})

@app.route('/api/kesupermarkets/<int:unitprice>', methods=['GET'])
def unitPrice(unitprice):
    
    return jsonify({'Unit Price': unitprice*2})


if __name__ == '__main__':  
    app.run(debug=True)  
