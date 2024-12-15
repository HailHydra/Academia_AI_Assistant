from flask import Flask, request, jsonify, render_template
from src.prompt import handle_prompt

app = Flask(__name__, static_folder="static", template_folder="templates")

@app.route('/')
def index():
    # Render the main HTML page
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    # Retrieve user input from JSON payload
    user_input = request.json.get('message', '')

    # Get the assistant's reply and optional image URL
    result = handle_prompt(user_input)

    # Prepare the JSON response
    response = {
        "response": result["response"]
    }
    if result.get("imageurl"):  # Include image URL if it exists
        response["imageurl"] = result["imageurl"]

    return jsonify(response)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000)