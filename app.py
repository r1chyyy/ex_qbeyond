from flask import Flask,request,g,Response, jsonify
from flask_expects_json import expects_json
import os

# Creates api app
app =   Flask(__name__)

# Validation schema for response
schema = {
  "type": "object",
  "properties": {
    "input1": { "type": "number" },
    "input2": { "type": "number" },
    "operator": { "type": "string" },
  },
  'required': ['input1', 'input2', 'operator']
}

# Calculation function
def calculate(input1, input2, operator):

    if operator == '+':
        return formatRes(input1 + input2)

    elif operator == '-':
        return formatRes(input1 - input2)

    elif operator == '*':
        return formatRes(input1 * input2)

    elif operator == '/':
        return formatRes(input1 / input2)
    else: 
        # On wrong operator type return bad response
        return Response("Wrong operator type",status=400)

# Formatting response to json
def formatRes(res):
    return jsonify({'result': res})

# Defining api route
@app.route('/calculate', methods = ['GET'])
@expects_json(schema)
def ReturnJSON():
    if(request.method == 'GET'):
        data = request.json
        res = calculate(data['input1'], data['input2'], data['operator'])
        return res

# Auto running app and server
if __name__=='__main__':
    # Enforcing port
    port = int(os.environ.get('PORT', 6000))
    app.run(host='0.0.0.0', port=port, debug=True)