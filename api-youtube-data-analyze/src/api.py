from flask import Flask, request, jsonify
from flask_cors import CORS
from start import Start
from log_tools import LogTools
import socket
socket.setdefaulttimeout(600) # seconds

start = Start()
log_tools = LogTools()

app = Flask(__name__)
CORS(app)

############# Endpoint que recebe os dados da pesquisa e inicia o processo de busca
@app.route('/search', methods=['POST'])
def search_api():
    log_tools.log_with_time_now('Start search')
    
    start.run_initial_search(request.json)
    return jsonify(None)
 
app.run(port=5000, host='localhost', debug=True)

