import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load the data from CSV file with the appropriate encoding
data = pd.read_csv('data.csv', encoding='utf-8')

# Write the dataset to a file
data.to_csv('dataset_formatted.txt', index=False)

# Print the dataset saved message
print("Dataset saved to 'dataset_formatted.txt'.")

# Preprocessing: Separate the features (message) and the target variable (category)
X = data['Message']
y = data['Category']

# Preprocessing: Convert the target variable to binary labels (0 for 'ham', 1 for 'spam')
y = y.map({'ham': 0, 'spam': 1})

# Preprocessing: Tokenize the text data and convert it into numerical feature vectors
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(X)

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(X_train, y_train)

# Make predictions on the test set
y_pred = classifier.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

# Print the accuracy
print("Accuracy:", accuracy)
