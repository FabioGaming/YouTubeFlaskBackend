import os
from flask import *
import json
os.system("set FLASK_ENV=development")
app = Flask(__name__)

@app.route('/get', methods=['GET'])
def GET_NOHeaders():
    headers = request.headers
    response = {
        "value": "Du hast es geschafft",
        "headers": str(headers)
    }
    return Response(json.dumps(response), status=200)

@app.route("/get/headers", methods=['GET'])
def GET_Headers():
    headers = request.headers
    if headers.get("myHeader") != None:
        response = {
            "value": "Du hast es geschafft",
            "headerValue": str(headers.get("myHeader")),
            "headers": str(headers)
        }

        return Response(json.dumps(response), status=200)
    else:
        return Response(json.dumps({ "value": "Du hast keinen header mit dem namen 'myHeader' angegeben!"}), status=403)

@app.route("/post", methods=['POST'])
def POST_NOSpecific():
    data = request.data
    response = {
        "value": "Du hast es geschafft!",
        "data": str(data)
    }
    return Response(json.dumps(response), status=200)


if __name__ == '__main__':
    app.run("0.0.0.0", 80)