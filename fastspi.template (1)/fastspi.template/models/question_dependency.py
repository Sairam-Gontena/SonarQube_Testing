"""
CREATE TABLE question_dependency (
    id uuid PRIMARY KEY,
    question_id varchar(255),
    dependent_question_id varchar(255),
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


class QuestionDependencyBase(Base):
    """A SQLAlchemy model class representing question_dependency table"""
    __tablename__ = 'question_dependency'
    id = Column('id', Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_id = Column('question_id', String(255), unique=True)
    dependent_question_id = Column('dependent_question_id', String(255))
    modified_by = Column('modified_by', String(255))
    modified_on = Column('modified_on', DateTime)
    live = Column('live', Boolean, default=True)
    version = Column('version', String(255))


class QuestionDependencyBaseModel(BaseModel):
    """Update this QuestionDependencyBaseModel to correspond to question_dependency sqlAlchemy model"""
    id: uuid.UUID
    question_id: str
    dependent_question_id: str
    modified_by: str
    modified_on: str
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True


class QuestionDependencyBaseModelCreateById(BaseModel):
    """Update this QuestionDependencyBaseModel to correspond to question_dependency sqlAlchemy model"""
    question_id: str
    dependent_question_id: str
    modified_by: str
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True
