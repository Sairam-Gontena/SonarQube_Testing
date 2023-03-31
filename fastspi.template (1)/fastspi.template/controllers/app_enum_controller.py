""" app_enum controller """
import datetime
import uuid

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.app_enum import AppEnumBaseModelCreateById, AppEnumBase
from config.database_connection import get_db

router = APIRouter()


@router.get("/")
def get_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Get By id"""
    query_obj = db.query(AppEnumBase).filter(AppEnumBase.id == id).all()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        return query_obj


@router.post("/")
def post_all(app_enum: AppEnumBaseModelCreateById, db: Session = Depends(get_db)):
    """Post ALL Data and create an id"""
    post_data = AppEnumBase(
        app_enum_type=app_enum.app_enum_type,
        app_enum_value=app_enum.app_enum_value)
    db.add(post_data)
    try:
        db.commit()
    except IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"{e.orig}")
    db.close()
    return {"message": "success"}


@router.put("/")
def update_by_id(id: uuid.UUID, app_enum: AppEnumBaseModelCreateById, db: Session = Depends(get_db)):
    """Update by Id"""
    query_obj = db.query(AppEnumBase).where(AppEnumBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="ID does not exist")
    else:
        app_enum.dict().update({"modified_on": f"{datetime.datetime.utcnow()}"})
        db.query(AppEnumBase).where(AppEnumBase.id == id).update(app_enum.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.patch("/")
def patch_by_id(id: uuid.UUID, app_enum: AppEnumBaseModelCreateById, db: Session = Depends(get_db)):
    """Patch by id"""
    query_obj = db.query(AppEnumBase).where(AppEnumBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(AppEnumBase).where(AppEnumBase.id == id).update(app_enum.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.delete("/")
def delete_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Delete by id"""
    query_obj = db.query(AppEnumBase).where(AppEnumBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(AppEnumBase).where(AppEnumBase.id == id).delete()
        db.commit()
    db.close()
    return {"message": "success"}


@router.get("/all")
def get_all(db: Session = Depends(get_db)):
    """Get all data as a list"""
    return db.query(AppEnumBase).all()


@router.get("/findByLive")
def is_live(live: bool, db: Session = Depends(get_db)):
    """Get live status"""
    return db.query(AppEnumBase).filter(AppEnumBase.live == live).all()
