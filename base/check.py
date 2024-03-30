import joblib
import os

# Load the SVC model

    # Load the SVC model
model_path = os.path.join(os.path.dirname(__file__), 'spam_detection', 'mySVCModel.pkl')
model = joblib.load(model_path)

# Test the model with some example inputs
example_messages = [
    "This is a normal message.",
    "Congratulations! You have won a free vacation. Click here to claim your prize!",
    "Hello, how are you today?"
]

for message in example_messages:
    is_spam = model.predict([message])
    print(f"Message: {message} | Is Spam: {is_spam}")
