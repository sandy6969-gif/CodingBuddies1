import joblib
import os

# Get the absolute path to the directory containing this file
dir_path = os.path.dirname(os.path.abspath(__file__))

# Load the ML model
model = joblib.load(os.path.join(dir_path, 'mySVCModel.pkl'))

def detect_spam(message):
    prediction = model.predict([message])[0]
    return prediction
