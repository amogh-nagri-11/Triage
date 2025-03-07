from sqlalchemy.orm import Session
from . import models, schemas

def create_patient(db: Session, patient_data: schemas.PatientCreate, severity: str):
    symptom_list = [s.lower().strip() for s in patient_data.symptoms]  # ✅ Normalize symptoms

    db_patient = models.Patient(
        name=patient_data.name.lower().strip(),
        age=patient_data.age,
        gender=patient_data.gender.lower().strip(),  # ✅ Normalize gender
        weight=patient_data.weight,
        heart_rate=patient_data.heart_rate,
        blood_pressure=patient_data.blood_pressure,
        temperature=patient_data.temperature,
        chief_complaint_chest_pain="chest pain" in symptom_list,
        chief_complaint_fever="fever" in symptom_list,
        chief_complaint_headache="headache" in symptom_list,
        chief_complaint_difficulty_breathing="difficulty breathing" in symptom_list,
        chief_complaint_abdominal_pain="abdominal pain" in symptom_list,
        severity=severity
    )
    db.add(db_patient)
    db.commit()
    db.refresh(db_patient)
    return db_patient
