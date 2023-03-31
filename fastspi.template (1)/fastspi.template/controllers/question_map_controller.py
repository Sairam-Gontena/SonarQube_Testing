""" question map controller """
import datetime
import uuid

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.question_map import QuestionMapBaseModelCreateById, QuestionMapBase
from config.database_connection import get_db

router = APIRouter()


@router.get("/")
def get_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Get By id"""
    query_obj = db.query(QuestionMapBase).filter(QuestionMapBase.id == id).all()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        return query_obj


@router.post("/")
def post_all(question_map: QuestionMapBaseModelCreateById, db: Session = Depends(get_db)):
    """Post ALL Data"""
    post_data = QuestionMapBase(id=uuid.uuid4(),
                                question_id=question_map.question_id,
                                parent_question_id=question_map.parent_question_id,
                                modified_on=datetime.datetime.utcnow(),
                                modified_by=question_map.modified_by,
                                live=question_map.live,
                                version=question_map.version)
    db.add(post_data)
    try:
        db.commit()
    except IntegrityError as e:
        raise HTTPException(status_code=422, detail=f"{e.orig}") from e
    db.close()
    return {"message": "success"}


@router.put("/")
def update_by_id(id: uuid.UUID, question_map: QuestionMapBaseModelCreateById, db: Session = Depends(get_db)):
    """Update by id"""
    query_obj = db.query(QuestionMapBase).where(QuestionMapBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        question_map.dict().update({"modified_on": f"{datetime.datetime.utcnow()}"})
        db.query(QuestionMapBase).where(QuestionMapBase.id == id).update(question_map.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.patch("/")
def patch_by_id(id: uuid.UUID, question_map: QuestionMapBaseModelCreateById, db: Session = Depends(get_db)):
    """Patch by id"""
    query_obj = db.query(QuestionMapBase).where(QuestionMapBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(QuestionMapBase).where(QuestionMapBase.id == id).update(question_map.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.delete("/")
def delete_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Delete by Id"""
    query_obj = db.query(QuestionMapBase).where(QuestionMapBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(QuestionMapBase).where(QuestionMapBase.id == id).delete()
        db.commit()
    db.close()
    return {"message": "success"}


@router.get("/all")
def get_question_map(db: Session = Depends(get_db)):
    """Get all data"""
    return db.query(QuestionMapBase).all()


@router.get("/findByLive")
def is_live(live=True, db: Session = Depends(get_db)):
    """Get live status"""
    return db.query(QuestionMapBase).filter(QuestionMapBase.live == live).all()
