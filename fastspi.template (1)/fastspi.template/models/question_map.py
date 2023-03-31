"""
CREATE TABLE question_map (
    id uuid PRIMARY KEY,
    question_id varchar(255),
    CONSTRAINT fk_question_map_question FOREIGN KEY(question_id) REFERENCES Question (question_sid),
    parent_question_id varchar(255),
    modified_by varchar(255),
    modified_on timestamp,
    live boolean,
    version varchar(255)
);
"""
import uuid

from sqlalchemy import Column, String, DateTime, Uuid, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

from models.question import QuestionBase

Base = declarative_base()
from pydantic import BaseModel


class QuestionMapBase(Base):
    """A SQLAlchemy model class representing question_map table"""
    __tablename__ = 'question_map'
    id = Column('id', Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    question_id = Column('question_id', String(255), ForeignKey(QuestionBase.question_sid))
    parent_question_id = Column('parent_question_id', String(255))
    modified_by = Column('modified_by', String(255))
    modified_on = Column('modified_on', DateTime)
    live = Column('live', Boolean, default=True)
    version = Column('version', String(255))


class QuestionMapBaseModel(BaseModel):
    """Update this QuestionMapBaseModel to correspond to question_map sqlAlchemy model"""
    id: uuid.UUID
    question_id: str
    parent_question_id: str
    modified_by: str
    modified_on: str
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True


class QuestionMapBaseModelCreateById(BaseModel):
    """Update this QuestionMapBaseModel to correspond to question_map sqlAlchemy model"""
    question_id: str
    parent_question_id: str
    modified_by: str
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True
