from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes


# Load the trained model
loaded_model = pickle.load(open('my_trained_model.pkl', 'rb'))
# Get the number of features from the model
if hasattr(loaded_model, 'n_features_in_'):
    total_features = loaded_model.n_features_in_
else:
    # Handle the case where the attribute is not available (you might set a default or raise an error)
    total_features = 20  # Set a default value or raise an error

DEFAULT_VALUE = 888



@app.route('/predict', methods=['POST'])
def predict():
    if request.content_type != 'application/json':
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    try:
        data = request.get_json()
    except Exception as e:
        return jsonify({'error': f'Invalid JSON data: {str(e)}'}), 400
    
    print(data)
    
    # Create an array filled with the default value
    # input_data = np.full(total_features, DEFAULT_VALUE)
    
    # # Set specific features manually using the feature names
    # feature_name_list = loaded_model.feature_names_in_
    # # print(feature_name_list)
    # index = 0
    # for feature_name in feature_name_list:
    #     if feature_name == 'procedure___0':
    #         input_data[index] = data['procedure___0']
    #     elif feature_name == 'procedure___12':
    #         input_data[index] = data['procedure___12']
    #     elif feature_name == 'procedure___2':
    #         input_data[index] = data['procedure___2']
    #     elif feature_name == 'procedure___8':
    #         input_data[index] = data['procedure___8']
    #     elif feature_name == 'procedure___7':
    #         input_data[index] = 0
        
    #     index += 1
            
 
    # # print(input_data)

    # # Make a prediction
    # try:
    #     prediction = loaded_model.predict(input_data.reshape(1, -1))[0]
        
    # except Exception as e:
    #     return jsonify({'error': f'Error making prediction: {str(e)}'}), 500
    # print("Prediction: ", prediction)
    # print("Prediction Prob: ", loaded_model.predict_proba(input_data.reshape(1, -1))[0])
    # prediction_prob = loaded_model.predict_proba(input_data.reshape(1, -1))[0]
    # return jsonify({'prediction_class0': prediction_prob[0], 'prediction_class1': prediction_prob[1]})
    return jsonify({"prediction": data})


if __name__ == '__main__':
    app.run(debug=True)
