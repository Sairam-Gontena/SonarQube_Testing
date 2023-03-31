"""
CREATE TABLE category_map (
    id uuid PRIMARY KEY,
    category_id varchar(255),
    CONSTRAINT fk_category FOREIGN KEY(category_id) REFERENCES Category (category_sid),
    parent_category_id varchar(255),
    sequence int,
    modified_by varchar(255),
    modified_on timestamp,
    live boolean,
    version varchar(255)
);
"""
import uuid
from datetime import datetime

from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, DateTime, Uuid, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base

from models.category import CategoryBase

Base = declarative_base()


class CategoryMapBase(Base):
    """A SQLAlchemy model class representing category_map table"""
    __tablename__ = 'category_map'
    id = Column('id', Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_id = Column('category_id', String(255), ForeignKey(CategoryBase.category_sid))
    parent_category_id = Column('parent_category_id', String(255))
    sequence = Column('sequence', Integer)
    modified_by = Column('modified_by', String(255))
    modified_on = Column('modified_on', DateTime)
    live = Column('live', Boolean, default=True)
    version = Column('version', String(255))


class CategoryMapBaseModel(BaseModel):
    """Update this basemodel to correspond to category_map sqlAlchemy model"""
    id: uuid.UUID
    category_id: str
    parent_category_id: str
    sequence: int
    modified_by: str
    modified_on: datetime
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True


class CategoryMapBaseModelCreateById(BaseModel):
    """Update this basemodel to correspond to category_map sqlAlchemy model"""
    category_id: str
    parent_category_id: str
    sequence: int
    modified_by: str
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True
