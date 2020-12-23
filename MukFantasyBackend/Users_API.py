from flask import Flask, Response,request
import json
from DBAPI import DBAPI
app = Flask(__name__)
'''
TODO: Some redundancy in the code I gotta clean
'''
@app.route('/')
def base():
    return Response(response=json.dumps({"Status": "UP"}),
                    status=200,
                    mimetype='application/json')

@app.route('/users', methods=['GET'])
def mongo_read():
    data = {"database": "fantasyfootball","collection": "users"}
    if data is None or data == {}:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = DBAPI(data)
    response = obj1.read()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')
  
@app.route('/musers', methods=['POST'])
def mongo_write():
    data = {"database": "fantasyfootball","collection": "users"}
    if data is None or data == {} or 'Document' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = DBAPI(data)
    response = obj1.write(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app.route('/users', methods=['PUT'])
def mongo_update():
    data = {"database": "fantasyfootball","collection": "users"}
    if data is None or data == {} or 'DataToBeUpdated' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = DBAPI(data)
    response = obj1.update()
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')

@app.route('/users', methods=['DELETE'])
def mongo_delete():
    data = {"database": "fantasyfootball","collection": "users"}
    if data is None or data == {} or 'Filter' not in data:
        return Response(response=json.dumps({"Error": "Please provide connection information"}),
                        status=400,
                        mimetype='application/json')
    obj1 = DBAPI(data)
    response = obj1.delete(data)
    return Response(response=json.dumps(response),
                    status=200,
                    mimetype='application/json')
if __name__ == '__main__':
    app.run(debug=True, port=5001, host='0.0.0.0')