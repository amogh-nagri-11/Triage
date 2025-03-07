from sqlalchemy import Column, Integer, String, Float, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Patient(Base):
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    age = Column(Integer, nullable=False)
    gender = Column(String(20), nullable=False)
    weight = Column(Float, nullable=False)
    heart_rate = Column(Integer, nullable=True)
    blood_pressure = Column(Integer, nullable=True)
    temperature = Column(Float, nullable=True)
    chief_complaint_chest_pain = Column(Boolean, default=False)
    chief_complaint_fever = Column(Boolean, default=False)
    chief_complaint_headache = Column(Boolean, default=False)
    chief_complaint_difficulty_breathing = Column(Boolean, default=False)
    chief_complaint_abdominal_pain = Column(Boolean, default=False)
    severity = Column(String(50), default="Unknown")

    def __repr__(self):
        return f"Patient(id={self.id}, name={self.name}, severity={self.severity})"
