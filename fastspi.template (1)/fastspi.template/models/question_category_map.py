"""
CREATE TABLE question_category_map (
    id uuid PRIMARY KEY,
    category_id varchar(255),
    CONSTRAINT fk_category_question FOREIGN KEY(category_id) REFERENCES Category (category_sid),
    question_id varchar(255),
    CONSTRAINT fk_question FOREIGN KEY(question_id) REFERENCES Question (question_sid),
    modified_by varchar(255),
    modified_on timestamp,
    live boolean,
    version varchar(255)
);
"""
import uuid

from pydantic import BaseModel
from sqlalchemy import Column, String, DateTime, Uuid, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

from models.category import CategoryBase
from models.question import QuestionBase

Base = declarative_base()


class QuestionCategoryMapBase(Base):
    """A SQLAlchemy model class representing question_category_map table"""
    __tablename__ = 'question_category_map'
    id = Column('id', Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_id = Column('category_id', String(255), ForeignKey(CategoryBase.category_sid))
    question_id = Column('question_id', String(255), ForeignKey(QuestionBase.question_sid))
    modified_by = Column('modified_by', String(255))
    modified_on = Column('modified_on', DateTime)
    live = Column('live', Boolean, default=True)
    version = Column('version', String(255))


class QuestionCategoryMapBaseModel(BaseModel):
    """Update this QuestionCategoryMapBaseModel to correspond to question_category_map sqlAlchemy model"""
    id: uuid.UUID
    category_id: str
    question_id: str
    modified_by: str
    modified_on: str
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True


class QuestionCategoryMapBaseModelCreateById(BaseModel):
    """Update this QuestionCategoryMapBaseModel to correspond to question_category_map sqlAlchemy model"""
    category_id: str
    question_id: str
    modified_by: str
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True
