"""
CREATE TABLE question (
    id uuid PRIMARY KEY,
    question_sid varchar(255) UNIQUE,
    question_display varchar(255),
    choice_group_id varchar(255) UNIQUE,
    modified_by varchar(255),
    modified_on timestamp,
    live boolean,
    version varchar(255)
);
"""
import uuid

from pydantic import BaseModel
from sqlalchemy import Column, String, DateTime, Uuid, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class QuestionBase(Base):
    """A SQLAlchemy model class representing question table"""
    __tablename__ = 'question'
    id = Column('id', Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_sid = Column('question_sid', String(255), unique=True)
    question_display = Column('question_display', String(255))
    choice_group_id = Column('choice_group_id', String(255), unique=True)
    modified_by = Column('modified_by', String(255))
    modified_on = Column('modified_on', DateTime)
    live = Column('live', Boolean, default=True)
    version = Column('version', String(255))


class QuestionBaseModel(BaseModel):
    """Update this PatientQuestionnaireBaseModel to correspond to question sqlAlchemy model"""
    id: uuid.UUID
    question_sid: str
    question_display: str
    choice_group_id: str
    modified_by: str
    modified_on: str
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True


class QuestionBaseModelCreateById(BaseModel):
    """Update this PatientQuestionnaireBaseModel to correspond to question sqlAlchemy model"""
    question_sid: str
    question_display: str
    choice_group_id: str
    modified_by: str
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True
