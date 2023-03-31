"""
CREATE TABLE questionnaire_template (
    id uuid PRIMARY KEY,
    category_id varchar(255),
    questionnaire_json varchar(255),
    modified_by varchar(255),
    modified_on timestamp,
    live boolean,
    version varchar(255)
);
"""
import uuid
from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import MetaData, Column, String, DateTime, Uuid, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()
metadata_obj = MetaData()


class QuestionnaireTemplateBase(Base):
    """A SQLAlchemy model class representing questionnaire_template table"""
    __tablename__ = 'questionnaire_template'
    id = Column('id', Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_id = Column('category_id', String(255))
    questionnaire_json = Column('questionnaire_json', String(255))
    modified_by = Column('modified_by', String(255))
    modified_on = Column('modified_on', DateTime)
    live = Column('live', Boolean, default=True)
    version = Column('version', String(255))


class QuestionnaireTemplateBaseModel(BaseModel):
    """Update this QuestionnaireTemplateBaseModel to correspond to questionnaire_template sqlAlchemy model"""
    id: uuid.UUID
    category_id: str
    questionnaire_json: str
    modified_by: str
    modified_on: datetime
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True


class QuestionnaireTemplateBaseModelCreateById(BaseModel):
    """Update this QuestionnaireTemplateBaseModel to correspond to questionnaire_template sqlAlchemy model"""
    category_id: str
    questionnaire_json: str
    modified_by: str
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True
