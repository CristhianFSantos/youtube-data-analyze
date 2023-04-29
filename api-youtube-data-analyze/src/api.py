from flask import Flask, request, jsonify
from flask_cors import CORS
from search import Search

search = Search()
app = Flask(__name__)
CORS(app)

@app.route('/search', methods=['POST'])
def search_api():
    search.print_search(request.json)
    return jsonify(None)

app.run(port=5000, host='localhost', debug=True)