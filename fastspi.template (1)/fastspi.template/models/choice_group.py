"""
CREATE TABLE choice_group (
    id uuid PRIMARY KEY,
    choice_group_sid varchar(255) UNIQUE,
    choice_group_name varchar(255),
    choice_type varchar(255),
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


class ChoiceGroupBase(Base):
    """A SQLAlchemy model class representing choice_group table"""
    __tablename__ = 'choice_group'
    id = Column('id', Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    choice_group_sid = Column('choice_group_sid', String(255), unique=True)
    choice_group_name = Column('choice_group_name', String(255))
    choice_type = Column('choice_type', String(255))
    modified_by = Column('modified_by', String(255))
    modified_on = Column('modified_on', DateTime)
    live = Column('live', Boolean, default=True)
    version = Column('version', String(255))


class ChoiceGroupBaseModel(BaseModel):
    """Update this basemodel to correspond to choice_group sqlAlchemy model"""
    id: uuid.UUID
    choice_group_sid: str
    choice_group_name: str
    choice_type: str
    modified_by: str
    modified_on: str
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True


class ChoiceGroupBaseModelCreateById(BaseModel):
    """Update this basemodel to correspond to choice_group sqlAlchemy model"""
    choice_group_sid: str
    choice_group_name: str
    choice_type: str
    modified_by: str
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True
