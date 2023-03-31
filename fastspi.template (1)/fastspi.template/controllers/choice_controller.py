""" choice controller """
import datetime
import uuid

# session is automatically closed with the URL associated with it at the end of block
from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.choice import ChoiceBaseModelCreateById, ChoiceBase
from config.database_connection import get_db

router = APIRouter()


@router.get("/")
def get_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Get By id"""
    query_obj = db.query(ChoiceBase).filter(ChoiceBase.id == id).all()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        return query_obj


@router.post("/")
def post_all(choice: ChoiceBaseModelCreateById, db: Session = Depends(get_db)):
    """Post ALL Data"""
    post_data = ChoiceBase(choice_sid=choice.choice_sid,
                           choice_group_id=choice.choice_group_id,
                           modified_on=datetime.datetime.utcnow(),
                           modified_by=choice.modified_by,
                           live=choice.live,
                           version=choice.version)
    db.add(post_data)
    try:
        db.commit()
    except IntegrityError as e:
        raise HTTPException(status_code=422, detail=f"{e.orig}") from e
    db.close()
    return {"message": "success"}


@router.put("/")
def update_by_id(id: uuid.UUID, choice: ChoiceBaseModelCreateById, db: Session = Depends(get_db)):
    """Update by id"""
    query_obj = db.query(ChoiceBase).where(ChoiceBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        choice.dict().update({"modified_on": f"{datetime.datetime.utcnow()}"})
        db.query(ChoiceBase).where(ChoiceBase.id == id).update(choice.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.patch("/")
def patch_by_id(id: uuid.UUID, choice: ChoiceBaseModelCreateById, db: Session = Depends(get_db)):
    """Patch by id"""
    query_obj = db.query(ChoiceBase).where(ChoiceBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(ChoiceBase).where(ChoiceBase.id == id).update(choice.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.delete("/")
def delete_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Delete by Id"""
    query_obj = db.query(ChoiceBase).where(ChoiceBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(ChoiceBase).where(ChoiceBase.id == id).delete()
        db.commit()
    db.close()
    return {"message": "success"}


@router.get("/all")
def get_all(db: Session = Depends(get_db)):
    """Get all data"""
    return db.query(ChoiceBase).all()


@router.get("/findByLive")
def is_live(live=True, db: Session = Depends(get_db)):
    """Get live status"""
    return db.query(ChoiceBase).filter(ChoiceBase.live == live).all()
