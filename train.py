import pickle
import xgboost as xgb
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


# Load the Iris dataset
iris = load_iris()
X = iris.data
y = iris.target


# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


# Define the XGBoost model
model = xgb.XGBClassifier(objective='multi:softmax', num_class=3)


# Train the model
model.fit(X_train, y_train)


# Save the trained model as a pickle file
with open('models/xgboost_model.pkl', 'wb') as file:
    pickle.dump(model, file)


# Make predictions on the test set
y_pred = model.predict(X_test)


# Calculate accuracy
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")