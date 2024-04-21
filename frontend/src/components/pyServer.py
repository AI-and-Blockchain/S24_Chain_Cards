from flask import Flask, jsonify
import sys
sys.path.append('C:/Users/13521/Desktop/chaincard/S24_Chain_Cards/backend/testing/truffle')
from alt_creator import generate_10_char
app = Flask(__name__)
def call_generate_10_char():
    generate_10_char()
    return

if __name__ == '__main__':
    app.run(debug=True)