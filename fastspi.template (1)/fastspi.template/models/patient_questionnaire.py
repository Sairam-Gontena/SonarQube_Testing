"""
CREATE TABLE patient_questionnaire (
    id uuid PRIMARY KEY,
    patient_id varchar(255),
    category_id varchar(255),
    response_json varchar(255),
    modified_by varchar(255),
    modified_on timestamp,
    live boolean,
    version varchar(255)
);
"""
import uuid
from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Column, String, DateTime, Uuid, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class PatientQuestionnaireBase(Base):
    """A SQLAlchemy model class representing patient_questionnaire table"""
    __tablename__ = 'patientquestionnaire'
    id = Column('id', Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    patient_id = Column('patient_id', String(255))
    category_id = Column('category_id', String(255))
    response_json = Column('response_json', String(255))
    modified_by = Column('modified_by', String(255))
    modified_on = Column('modified_on', DateTime)
    live = Column('live', Boolean, default=True)
    version = Column('version', String(255))


class PatientQuestionnaireBaseModel(BaseModel):
    """Update this PatientQuestionnaireBaseModel to correspond to patient_questionnaire sqlAlchemy model"""
    id: uuid.UUID
    patient_id: str
    category_id: str
    response_json: str
    modified_by: str
    modified_on: datetime
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True


class PatientQuestionnaireBaseModelCreateById(BaseModel):
    """Update this PatientQuestionnaireBaseModel to correspond to patient_questionnaire sqlAlchemy model"""
    patient_id: str
    category_id: str
    response_json: str
    modified_by: str
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True
