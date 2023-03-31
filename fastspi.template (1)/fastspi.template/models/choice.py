"""
CREATE TABLE choice (
    id uuid PRIMARY KEY,
    choice_sid varchar(255) UNIQUE,
    CONSTRAINT fk_choice FOREIGN KEY(choice_group_id) REFERENCES ChoiceGroup (choice_group_sid),
    sequence int,
    modified_by varchar(255),
    modified_on timestamp,
    live boolean,
    version varchar(255)
);
"""
import uuid

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, Uuid, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

from models.choice_group import ChoiceGroupBase

Base = declarative_base()


class ChoiceBase(Base):
    """A SQLAlchemy model class representing choice table"""
    __tablename__ = 'choice'
    id = Column('id', Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    choice_sid = Column('choice_sid', String(255), unique=True)
    choice_group_id = Column('choice_group_id', String(255), ForeignKey(ChoiceGroupBase.choice_group_sid))
    sequence = Column('sequence', Integer)
    modified_by = Column('modified_by', String(255))
    modified_on = Column('modified_on', DateTime)
    live = Column('live', Boolean, default=True)
    version = Column('version', String(255))


class ChoiceBaseModel(BaseModel):
    """Update this basemodel to correspond to choice sqlAlchemy model"""
    id: uuid.UUID
    choice_sid: str
    choice_group_id: str
    sequence: int
    modified_by: str
    modified_on: str
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True


class ChoiceBaseModelCreateById(BaseModel):
    """Update this basemodel to correspond to choice sqlAlchemy model"""
    choice_sid: str
    choice_group_id: str
    sequence: int
    modified_by: str
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True
