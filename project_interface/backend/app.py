from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


# Load the trained model
loaded_model = pickle.load(open('my_trained_model.pkl', 'rb'))

@app.route('/predict', methods=['GET','POST'])
def predict():
    # data = "ham"
    data = request.get_json()  
    print(data)
    # input_data = np.array([data['feature1'], data['feature2'], ...]) 

    # Preprocess input_data if necessary
    # Make predictions using the loaded model
    # prediction = loaded_model.predict(input_data.reshape(1, -1))[0]

    return jsonify({'prediction': data})


if __name__ == '__main__':
    app.run(debug=True)
