from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

def load_state():
    with open('state.json', 'r') as f:
        return json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/state')
def get_state():
    return jsonify(load_state())

if __name__ == '__main__':
    app.run(debug=True, port=5000)