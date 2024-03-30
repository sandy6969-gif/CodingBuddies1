import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Embedding, Conv1D, GlobalMaxPooling1D, Dense, Dropout
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

# Load your own dataset
dataset = pd.read_csv('spam.csv', encoding='latin-1')
dataset = dataset.drop(["Unnamed: 2", "Unnamed: 3", "Unnamed: 4"], axis=1)
dataset = dataset.rename(columns={"v1": "label", "v2": "text"})
dataset['label'] = dataset.label.map({'ham': 0, 'spam': 1})

# Tokenize the text and create word index
tokenizer = tf.keras.preprocessing.text.Tokenizer()
tokenizer.fit_on_texts(dataset['text'])
vocab_size = len(tokenizer.word_index) + 1
max_seq_length = max([len(text.split()) for text in dataset['text']])

# Convert text to numerical sequences
sequences = tokenizer.texts_to_sequences(dataset['text'])
sequences = tf.keras.preprocessing.sequence.pad_sequences(sequences, maxlen=max_seq_length)

# Split the data into train and test sets
x_train, x_test, y_train, y_test = train_test_split(sequences, dataset['label'], test_size=0.2, random_state=42)

# Build the CNN model
embedding_dim = 50
model = Sequential()
model.add(Embedding(input_dim=vocab_size, output_dim=embedding_dim, input_length=max_seq_length))
model.add(Conv1D(filters=64, kernel_size=5, activation='relu'))
model.add(GlobalMaxPooling1D())
model.add(Dense(128, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

# Compile the model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Train the model
model.fit(x_train, y_train, epochs=10, batch_size=32, validation_split=0.1)

# Evaluate the model
y_pred = model.predict(x_test)
y_pred = (y_pred >= 0.5).astype(int)
print("Test Accuracy:", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred))
print("Recall:", recall_score(y_test, y_pred))
print("F1-score:", f1_score(y_test, y_pred))
