from flask import Flask, request, jsonify
from flask_cors import CORS
from start import Start
import socket
socket.setdefaulttimeout(600) # seconds

start = Start()
app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search_api():
    start.run_initial_search(request.json)
    return jsonify(None)
 
app.run(port=5000, host='localhost', debug=True)

