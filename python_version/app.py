# app.py – Flask Backend Server for MNOA Web App
# ------------------------------------------------
# This script launches a lightweight Flask server to:
# 1. Serve the static frontend (HTML UI)
# 2. Accept POST requests at /disambiguate with medication name input
# 3. Return JSON-formatted disambiguation results from the backend module

from flask import Flask, request, jsonify, send_from_directory
from mnoa_backend_module import run_mnoa  # Import main logic function

# Initialize Flask app with current directory as static folder
app = Flask(__name__, static_folder='.', static_url_path='')

# Route: Serve Frontend UI (GET /)
@app.route('/')
def serve_frontend():
    return send_from_directory('.', 'frontend.html')  # Delivers frontend.html to browser

# Route: Process Disambiguation Request (POST /disambiguate)
@app.route('/disambiguate', methods=['POST'])
def disambiguate():
    data = request.get_json()                      # Get JSON input from frontend
    names = data.get("names", [])                  # Extract 'names' list (default to empty list)
    result = run_mnoa(names)                       # Run MNOA algorithm on input list
    return jsonify(result)                         # Return output as JSON response

# Run app when this file is executed directly (not imported)
if __name__ == '__main__':
    app.run(debug=True, port=5050, use_reloader=False)  # Start local server at http://localhost:5050
