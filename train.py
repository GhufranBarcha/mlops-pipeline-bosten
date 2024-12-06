import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import joblib

# Load and prepare data
df = pd.read_csv("BostonHousing.csv")
print(df)

X = df.drop(columns=["medv"])  # Drop the target column to get the features
y = df["medv"]  

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluate model
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Save model
joblib.dump(model, "model.pkl")
print("Model saved as model.pkl")
