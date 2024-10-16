from flask import Flask, jsonify
import requests

# Initialize the application
app = Flask(__name__)

@app.route('/call-api', methods=['GET'])
def call_external_api():
    # URL of the external API you want to call
    api_url = 'https://jsonplaceholder.typicode.com/posts'
    
    try:
        # Make the external API request
        response = requests.get(api_url)
        response.raise_for_status()  # Check for HTTP errors
        
        # Process and return the data
        data = response.json()  # Assuming the API response is JSON
        return jsonify(data)
    
    except requests.exceptions.RequestException as e:
        # Handle any errors
        return jsonify({'error': str(e)}), 500

# Run the application
if __name__ == '__main__':
    app.run(debug=True)