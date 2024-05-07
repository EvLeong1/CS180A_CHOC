import tensorflow as tf
from tensorflow import keras
import pandas as pd
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, Dropout, BatchNormalization
from keras.optimizers import Adam
from keras.callbacks import EarlyStopping
from sklearn.model_selection import KFold
import pickle

df = pd.read_excel("imputed_dataset.xlsx")

# Define features (X) and target variable (y)
X = df.drop("target", axis=1)
y = df["target"]

# Define the number of features
num_features = len(df.columns) - 1
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Model definition
model = Sequential([
    Dense(256, input_dim=num_features, activation='relu'),
    BatchNormalization(),
    Dense(512, activation='relu'),
    Dropout(0.45),
    BatchNormalization(),
    Dense(256, activation='relu'),
    Dropout(0.45),
    BatchNormalization(),
    Dense(128, activation='relu'),
    Dropout(0.45),
    BatchNormalization(),
    Dense(64, activation='relu'),
    Dropout(0.45),
    BatchNormalization(),
    Dense(1, activation='sigmoid')
])

model.summary()

opt = Adam(learning_rate=0.001)
model.compile(optimizer=opt, loss='binary_crossentropy', metrics=['accuracy'])

# Define early stopping to prevent overfitting
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

# Train the model with k-fold cross-validation
kf = KFold(n_splits=5, shuffle=True, random_state=42)
for train_index, val_index in kf.split(X_train):
    X_train_fold, X_val_fold = X_train.iloc[train_index], X_train.iloc[val_index]
    y_train_fold, y_val_fold = y_train.iloc[train_index], y_train.iloc[val_index]

    history = model.fit(X_train_fold, y_train_fold, epochs=100, batch_size=64,
                        validation_data=(X_val_fold, y_val_fold), callbacks=[early_stopping])

# Evaluate the model on the test set
loss, accuracy = model.evaluate(X_test, y_test)
print("Test Loss:", loss)
print("Test Accuracy:", accuracy)

# Save the trained model to a pickle file
with open('my_trained_model.pkl', 'wb') as f:
    pickle.dump(model, f)
