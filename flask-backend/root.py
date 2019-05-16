from flask import Flask, request
import json
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    jsonResp = {'jack': 4098, 'sape': 4139}
    print(json.dumps(jsonResp))
    return json.dumps(jsonResp)

if __name__== '__main__':
    app.run()