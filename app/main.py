from fastapi import FastAPI, Depends, Body
from sqlalchemy.orm import Session
from .database import get_db
from . import schemas, crud
from .ai_models import model, predict_triage
from .routers import triage  

app = FastAPI()
app.include_router(triage.router)

@app.post("/predict")
def predict_and_store(
    patient: schemas.PatientCreate = Body(..., embed=True),  # ✅ Ensure FastAPI correctly reads the request body
    db: Session = Depends(get_db)
):
    severity = predict_triage(
        model,
        age=patient.age,
        weight=patient.weight,
        gender=patient.gender,
        symptoms=patient.symptoms
    )
    db_patient = crud.create_patient(db, patient, severity)
    return {"id": db_patient.id, "name": db_patient.name, "predicted_severity": severity}

# ✅ Debugging Route to Test Request Body
@app.post("/debug")
async def debug_request(data: dict = Body(...)):
    return {"received_data": data}
