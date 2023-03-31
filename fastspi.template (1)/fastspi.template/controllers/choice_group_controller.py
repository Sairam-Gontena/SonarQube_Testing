""" choice group controller """
import datetime
import uuid

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.choice_group import ChoiceGroupBaseModelCreateById, ChoiceGroupBase
from config.database_connection import get_db

router = APIRouter()


@router.get("/")
def get_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Get By id"""
    query_obj = db.query(ChoiceGroupBase).filter(ChoiceGroupBase.id == id).all()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        return query_obj


@router.post("/")
def post_all(choice_group: ChoiceGroupBaseModelCreateById, db: Session = Depends(get_db)):
    """Post ALL Data"""
    post_data = ChoiceGroupBase(choice_group_sid=choice_group.choice_group_sid,
                                choice_group_name=choice_group.choice_group_name,
                                choice_type=choice_group.choice_type,
                                modified_on=datetime.datetime.utcnow(),
                                modified_by=choice_group.modified_by,
                                live=choice_group.live,
                                version=choice_group.version)
    db.add(post_data)
    try:
        db.commit()
    except IntegrityError as e:
        raise HTTPException(status_code=422, detail=f"{e.orig}")
    db.close()
    return {"message": "success"}


@router.put("/")
def update_by_id(id: uuid.UUID, choice_group: ChoiceGroupBaseModelCreateById, db: Session = Depends(get_db)):
    """Update by id"""
    query_obj = db.query(ChoiceGroupBase).where(ChoiceGroupBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        choice_group.dict().update({"modified_on": f"{datetime.datetime.utcnow()}"})
        db.query(ChoiceGroupBase).where(ChoiceGroupBase.id == id).update(choice_group.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.patch("/")
def patch_by_id(id: uuid.UUID, choice_group: ChoiceGroupBaseModelCreateById, db: Session = Depends(get_db)):
    """Patch by Id"""
    query_obj = db.query(ChoiceGroupBase).where(ChoiceGroupBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(ChoiceGroupBase).where(ChoiceGroupBase.id == id).update(choice_group.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.delete("/")
def delete_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Delete by Id"""
    query_obj = db.query(ChoiceGroupBase).where(ChoiceGroupBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(ChoiceGroupBase).where(ChoiceGroupBase.id == id).delete()
        db.commit()
    db.close()
    return {"message": "success"}


@router.get("/all")
def get_choice_group(db: Session = Depends(get_db)):
    """Get all data"""
    return db.query(ChoiceGroupBase).all()


@router.get("/findByLive")
def is_live(live=True, db: Session = Depends(get_db)):
    """Get live status"""
    return db.query(ChoiceGroupBase).filter(ChoiceGroupBase.live == live).all()
