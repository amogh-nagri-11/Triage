from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List  # Ensure compatibility with Python < 3.9
from app.database import get_db
from app.ai_models import predict_triage, model  # Import model
from app.models import Patient

router = APIRouter()

@router.post("/predict")
def predict_triage_api(
    name: str,
    age: int,
    gender: str,
    weight: float,
    symptoms: List[str],  # Fixed for Python < 3.9
    db: Session = Depends(get_db),
):
    """API endpoint to predict triage severity"""
    prediction = predict_triage(model, age, weight, gender, symptoms)  # Fixed function call
    
    # Save patient record in the database
    new_patient = Patient(
        name=name,
        age=age,
        gender=gender,
        weight=weight,
        chief_complaint_chest_pain="Chest Pain" in symptoms,
        chief_complaint_fever="Fever" in symptoms,
        chief_complaint_headache="Headache" in symptoms,
        chief_complaint_difficulty_breathing="Difficulty Breathing" in symptoms,
        chief_complaint_abdominal_pain="Abdominal Pain" in symptoms,
        severity=prediction,
    )
    db.add(new_patient)
    db.commit()
    
    return {"name": name, "predicted_severity": prediction}
