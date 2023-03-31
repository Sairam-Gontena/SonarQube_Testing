"""
CREATE TABLE category (
    id uuid PRIMARY KEY,
    category_sid varchar(255) UNIQUE,
    category_name varchar(255),
    modified_on timestamp,
    modified_by varchar(255),
    live boolean,
    version varchar(255)
);
"""
import uuid

from pydantic import BaseModel
from sqlalchemy import Column, String, DateTime, Uuid, Boolean
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class CategoryBase(Base):
    """A SQLAlchemy model class representing category table"""
    __tablename__ = 'category'
    id = Column('id', Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    category_sid = Column('category_sid', String(255), unique=True)
    category_name = Column('category_name', String(255))
    modified_on = Column('modified_on', DateTime)
    modified_by = Column('modified_by', String(255))
    live = Column('live', Boolean, default=True)
    version = Column('version', String(255))


class CategoryBaseModel(BaseModel):
    """Update this basemodel to correspond to category sqlAlchemy model"""
    id: uuid.UUID
    category_sid: str
    category_name: str
    modified_on: str
    modified_by: str
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True


class CategoryBaseModelCreateById(BaseModel):
    """Update this basemodel to correspond to category sqlAlchemy model"""
    category_sid: str
    category_name: str
    modified_by: str
    live: bool
    version: str

    class Config:
        """Add model to ORM"""
        orm_mode = True
