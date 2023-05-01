from flask import Flask, request, jsonify
import numpy as np
import pickle

model = pickle.load(open('model.pkl', 'rb'))
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"


@app.route('/predict', methods=['POST'])
def predict():
    sentence = request.form.get('sentence')
    # iq = request.form.get('iq')
    # profile_score = request.form.get('profile_score')
    input_query = sentence
    print(sentence)
    result = model.augment(input_phrase=sentence)[0][0]
    return jsonify({'placement': str(result)})


if __name__ == '__main__':
    app.run(debug=True)
