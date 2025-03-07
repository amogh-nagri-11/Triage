from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#Database URL (NO PASSWORD, as per your setup)
DATABASE_URL = "postgresql://triage_user:triage@localhost:5432/triage_db"

engine = create_engine(DATABASE_URL)

# Create a session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Dependency to get a session
def get_db():
    db = SessionLocal()
    try:
        yield db  # Provides a database session
    finally:
        db.close()  # Closes session after use
