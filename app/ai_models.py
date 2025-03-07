import joblib
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

# Define symptoms used in training
SYMPTOMS_LIST = [
    "Chest Pain", "Headache", "Fever", "Cough", "Abdominal Pain",
    "Difficulty Breathing", "Dizziness", "Fatigue", "Nausea", "Weakness"
]

def train_triage_model(csv_path, output_model_path="models/triage_model.pkl"):
    df = pd.read_csv(csv_path)

    # Encode gender
    df["gender_encoded"] = df["gender"].map({"Male": 1, "Female": 0})

    # One-hot encode symptoms
    for symptom in SYMPTOMS_LIST:
        df[symptom] = df["symptoms"].apply(lambda x: 1 if symptom in x else 0)

    # Select features and target
    X = df[["age", "weight", "gender_encoded"] + SYMPTOMS_LIST]
    y = df["triage_level"]

    # Train model
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Evaluate
    print("Model Performance:\n", classification_report(y_test, model.predict(X_test)))

    # Save model
    joblib.dump(model, output_model_path)

def predict_triage(model, age, weight, gender, symptoms):
    gender_encoded = 1 if gender.lower() == "male" else 0
    symptoms_vector = [1 if symptom in symptoms else 0 for symptom in SYMPTOMS_LIST]
    input_features = np.array([[age, weight, gender_encoded] + symptoms_vector])
    input_df = pd.DataFrame(input_features, columns=["age", "weight", "gender_encoded"] + SYMPTOMS_LIST)
    return model.predict(input_df)[0]

# Load model globally
model = joblib.load("models/triage_model.pkl")
