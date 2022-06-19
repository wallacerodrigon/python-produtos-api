from flask import Flask
from flask import jsonify
import json
app = Flask(__name__)
@app.route('/')
def hello_world():
    return 'Hello World!'

# read file
with open('/Volumes/DADOS/desenvolvimento/workspace/python/basico_python/webserver/database.json', 'r') as myfile:
    data=myfile.read()
# parse file
obj = json.loads(data)
@app.route('/todo/getall',methods=['GET'])
def getTasks():
    return jsonify(obj)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=8080)

