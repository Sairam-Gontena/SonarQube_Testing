"""
CREATE TABLE app_enum (
    id uuid PRIMARY KEY,
    app_enum_type varchar(255),
    app_enum_value varchar(255)
);
"""
import uuid

from pydantic import BaseModel
from sqlalchemy import Column, String, Uuid
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class AppEnumBase(Base):
    """A SQLAlchemy model class representing app_enum table"""
    __tablename__ = 'app_enum'
    id = Column('id', Uuid(as_uuid=True), primary_key=True, default=uuid.uuid4)
    app_enum_type = Column('app_enum_type', String(255))
    app_enum_value = Column('app_enum_value', String(255))


class AppEnumBaseModel(BaseModel):
    """Update this basemodel to correspond to app_enum sqlAlchemy model"""
    id: uuid.UUID
    app_enum_type: str
    app_enum_value: str

    class Config:
        """Add model to ORM"""
        orm_mode = True


class AppEnumBaseModelCreateById(BaseModel):
    """Update this basemodel to correspond to app_enum sqlAlchemy model"""
    app_enum_type: str
    app_enum_value: str

    class Config:
        """Add model to ORM"""
        orm_mode = True
