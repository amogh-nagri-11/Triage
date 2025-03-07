from sqlalchemy.orm import Session
from . import models, schemas

def create_patient(db: Session, patient_data: schemas.PatientCreate, severity: str):
    db_patient = models.Patient(
        name=patient_data.name,
        age=patient_data.age,
        gender=patient_data.gender,
        weight=patient_data.weight,
        heart_rate=patient_data.heart_rate,
        blood_pressure=patient_data.blood_pressure,
        temperature=patient_data.temperature,
        chief_complaint_chest_pain="Chest Pain" in patient_data.symptoms,
        chief_complaint_fever="Fever" in patient_data.symptoms,
        chief_complaint_headache="Headache" in patient_data.symptoms,
        chief_complaint_difficulty_breathing="Difficulty Breathing" in patient_data.symptoms,
        chief_complaint_abdominal_pain="Abdominal Pain" in patient_data.symptoms,
        severity=severity
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient
