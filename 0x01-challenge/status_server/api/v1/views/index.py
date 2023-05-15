#!/usr/bin/python3
""" Index view
"""
from flask import jsonify

def status():
    """ Status of the web server
    """
    return jsonify({"status": "OK"})
