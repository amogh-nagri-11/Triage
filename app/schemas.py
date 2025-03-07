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
    symptoms: List[str]  # Ensure symptoms is a List

    class Config:
        from_attributes = True  # Ensure compatibility with SQLAlchemy models

class PatientResponse(PatientCreate):
    id: int  # Include ID field for responses
    severity: str  # Include predicted severity

    class Config:
        from_attributes = True  # Ensure proper ORM conversion
