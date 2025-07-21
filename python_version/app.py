from flask import Flask, request, jsonify, send_from_directory
from mnoa_backend_module import run_mnoa

app = Flask(__name__, static_folder='.', static_url_path='')

@app.route('/')
def serve_frontend():
    return send_from_directory('.', 'frontend.html')

@app.route('/disambiguate', methods=['POST'])
def disambiguate():
    data = request.get_json()
    names = data.get("names", [])
    result = run_mnoa(names)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True, port=5050, use_reloader=False)
