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
    input_data = np.full(total_features, DEFAULT_VALUE)
    
    # # Set specific features manually using the feature names
    feature_name_list = loaded_model.feature_names_in_
    # print(feature_name_list)
    
    
     # Calculate the rate of change for hemoglobin
    initial_hb = int(data['initial_hb'])
    current_hb = int(data['current_hb'])
    hours_admit = int(data['hours_admit'])
    
    if initial_hb is not None and current_hb is not None and hours_admit is not None:
        rate_of_change = (current_hb - initial_hb) / ((hours_admit/5)-1)
        running_roc = initial_hb
        # print(rate_of_change)
        
        index = feature_name_list.tolist().index('hb_0-4.99')
        for i in range(0, round(hours_admit/5)):
            if i == 0:
                print("Initial HB: ", initial_hb)
                input_data[index] = initial_hb
                index+=1
            else:
                input_data[index] = running_roc + rate_of_change
                running_roc = running_roc + rate_of_change
                index+=1
                
            
                
                
    index = 0
    for feature_name in feature_name_list:
        if feature_name == 'los_floor':
            input_data[index] = data['los_floor']
        elif feature_name == 'mtp':
            input_data[index] = data['mtp']
        elif feature_name == 'sbp_lowptc':
            input_data[index] = data['sbp_low']
        elif feature_name == 'dbp_lowptc':
            input_data[index] = data['dbp_low']
    
            
        
        index += 1
            
 
    # print(input_data)

    # # Make a prediction
    try:
        prediction = loaded_model.predict(input_data.reshape(1, -1))[0]
        
        
    except Exception as e:
        return jsonify({'error': f'Error making prediction: {str(e)}'}), 500
    print("Prediction: ", prediction)
    print("Prediction Prob: ", loaded_model.predict_proba(input_data.reshape(1, -1))[0])
    prediction_prob = loaded_model.predict_proba(input_data.reshape(1, -1))[0]
    return jsonify({'prediction_class0': prediction_prob[0], 'prediction_class1': prediction_prob[1]})
    
    # return jsonify({"prediction": data})


if __name__ == '__main__':
    app.run(debug=True)
