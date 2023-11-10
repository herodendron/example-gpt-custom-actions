from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, World hey hey!'

@app.route('/about')
def about():
    return 'About'

@app.route('/process_data', methods=['POST'])
def process_data():
    data = request.get_json()

    # Extracting string and integer from the JSON data
    string_data = data.get('str_data')
    int_data = data.get('int_data')

    # You can perform any operation here. For simplicity, just returning the data.
    return jsonify({
        "Received String": string_data,
        "Received Integer": int_data
    })

if __name__ == '__main__':
    app.run(debug=True)
