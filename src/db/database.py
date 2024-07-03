from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Base
import os

# Establish database connection to PostgreSQL using SQLAlchemy.
engine = create_engine('postgresql+psycopg2://postgres:123@localhost/ActivosIntelectualesBD')

#DATABASE_URL = os.getenv('DATABASE_URL')
#engine = create_engine(DATABASE_URL)

# Configure session factory to manage database transactions.
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def init_db():
    """
    Initialize the database schema.

    Executes SQL commands to create tables defined in Base metadata, 
    setting up the necessary database structure.
    """
    Base.metadata.create_all(bind=engine)

def get_db():
    """
    Manage database session lifecycle.

    Yields a session from SessionLocal, ensuring proper opening and closing within 
    a context manager to prevent resource leaks and manage database connections efficiently.
    """
    db = SessionLocal()  # Initialize a session
    try:
        yield db  # Yield session control to the caller
    finally:
        db.close()  # Close session after use
