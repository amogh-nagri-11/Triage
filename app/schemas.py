from pydantic import BaseModel
from typing import List, Optional

class PatientCreate(BaseModel):
    name: str
    age: int
    gender: str  # "Male" or "Female"
    weight: float
    heart_rate: Optional[int] = None
    blood_pressure: Optional[int] = None
    temperature: Optional[float] = None
    symptoms: List[str]

class PatientResponse(PatientCreate):
    severity: str
