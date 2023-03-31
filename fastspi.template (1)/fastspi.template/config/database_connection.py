"""This file holds database connection and engine objects"""
from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

database_connection_url = URL.create(
    drivername="postgresql",
    username="postgres",
    password="password",
    host="localhost",
    database="test_db_constance"
)
engine = create_engine(database_connection_url)
connection = engine.connect()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    """Dependency to create multiple sessions
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
