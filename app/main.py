from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from .database import get_db
from . import schemas, crud
from .ai_model import model, predict_triage

app = FastAPI()

@app.post("/predict")
def predict_and_store(patient: schemas.PatientCreate, db: Session = Depends(get_db)):
    severity = predict_triage(
        model,
        age=patient.age,
        weight=patient.weight,
        gender=patient.gender,
        symptoms=patient.symptoms
    )
    db_patient = crud.create_patient(db, patient, severity)
    return {"id": db_patient.id, "name": db_patient.name, "predicted_severity": severity}
