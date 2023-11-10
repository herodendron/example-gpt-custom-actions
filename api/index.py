from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World hey hey!'

@app.route('/about')
def about():
    return 'About'

@app.route('/get-weather', methods=['POST'])
def get_weather():
    # Expecting a JSON payload with a key 'location'
    data = request.get_json()
    location = data.get('location')

    if not location:
        return jsonify({"error": "Location is required"}), 400

    # Example response, you would replace this with actual weather data retrieval logic
    weather_data = {"location": location, "temperature": "23°C", "condition": "Sunny"}

    return jsonify(weather_data)

if __name__ == '__main__':
    app.run(debug=True)
