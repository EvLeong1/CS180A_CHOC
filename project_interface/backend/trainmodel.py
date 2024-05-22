import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder
from sklearn.neural_network import MLPClassifier
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import cross_val_score, KFold
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import export_graphviz
import pydotplus
from IPython.display import Image
import seaborn as sns

import pickle

df = pd.read_excel("imputed_dataset.xlsx")
# Define features (X) and target variable (y)

test_df = df.sample(n=100, random_state=42)
df = df.drop(test_df.index)
test_df = test_df.copy()

test_df_X = test_df.drop("target", axis=1)
test_df_y = test_df["target"]

X = df.drop("target", axis=1)
y = df["target"]
# Define the number of features# Importing necessary libraries


# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize the DecisionTreeClassifier
dtree = DecisionTreeClassifier()

# Fit the model on the training data
dtree.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = dtree.predict(X_test)



# --- Getting misclassifications ---

# Resulting classifications
results_df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})

# Getting rows that were misclassified
misclassified_indices = results_df.index[results_df['Actual'] != results_df['Predicted']]
misclassified_data = df.loc[misclassified_indices]

# add indices to the table
misclassified_data['index'] = misclassified_indices
# sort by indices
misclassified_data = misclassified_data.sort_values(by='index')
# export to excel
misclassified_data.to_excel("misclassified_data.xlsx", index=False)


# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

rf_classifier = RandomForestClassifier(n_estimators=150,
                                       criterion='gini',
                                       max_depth=15,
                                       min_samples_split=2,
                                       min_samples_leaf=1,
                                       bootstrap=True,
                                       random_state=42)

kf = KFold(n_splits=10, shuffle=True, random_state=42)

cv_scores = cross_val_score(rf_classifier, X, y, cv=kf)

print("Cross-validation scores:", cv_scores)

# Fit the model on the training data
rf_classifier.fit(X, y)

# Make predictions on the testing data
y_pred = rf_classifier.predict(X)

feature_importances = pd.DataFrame({'Feature': X.columns, 'Importance': rf_classifier.feature_importances_})

# Sort feature importances by importance score
feature_importances = feature_importances.sort_values('Importance', ascending=False)
print(feature_importances)


# Resulting classifications
results_df = pd.DataFrame({'Actual': y, 'Predicted': y_pred})

# Getting rows that were misclassified
misclassified_indices = results_df.index[results_df['Actual'] != results_df['Predicted']]
misclassified_data = df.loc[misclassified_indices]

# add indices to the table
misclassified_data['index'] = misclassified_indices
# sort by indices
misclassified_data = misclassified_data.sort_values(by='index')
# export to excel
misclassified_data.to_excel("misclassified_data.xlsx", index=False)

# Save the trained model to a pickle file
with open('my_trained_model.pkl', 'wb') as f:
    pickle.dump(rf_classifier, f)
