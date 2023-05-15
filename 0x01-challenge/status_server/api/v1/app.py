#!/usr/bin/python3
"""
Web server 
"""
from api.v1.views.index import status
from flask import Flask, jsonify, make_response

app = Flask(__name__)

@app.route('/api/v1/status', methods=['GET'], strict_slashes=False)
def status_route():
    return status()



@app.errorhandler(404)
def not_found(error):
    """ json 404 page """
    return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == "__main__":
    # python -m api.v1.app 
    app.run(host="0.0.0.0", port=5000)
