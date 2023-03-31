""" question category map controller """
import datetime
import uuid

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.question_category_map import QuestionCategoryMapBaseModelCreateById, QuestionCategoryMapBase
from config.database_connection import get_db

router = APIRouter()


@router.get("/")
def get_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Get By id"""
    query_obj = db.query(QuestionCategoryMapBase).filter(QuestionCategoryMapBase.id == id).all()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        return query_obj


@router.post("/")
def post_all(question: QuestionCategoryMapBaseModelCreateById, db: Session = Depends(get_db)):
    """Post ALL Data"""
    post_data = QuestionCategoryMapBase(category_id=question.category_id,
                                        question_id=question.question_id,
                                        modified_on=datetime.datetime.utcnow(),
                                        modified_by=question.modified_by,
                                        live=question.live,
                                        version=question.version)
    db.add(post_data)
    try:
        db.commit()
    except IntegrityError as e:
        raise HTTPException(status_code=422, detail=f"{e.orig}")
    db.close()
    return {"message": "success"}


@router.put("/")
def update_by_id(id: uuid.UUID, question: QuestionCategoryMapBaseModelCreateById, db: Session = Depends(get_db)):
    """Update by id"""
    query_obj = db.query(QuestionCategoryMapBase).where(QuestionCategoryMapBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        question.dict().update({"modified_on": f"{datetime.datetime.utcnow()}"})
        db.query(QuestionCategoryMapBase).where(QuestionCategoryMapBase.id == id).update(question.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.patch("/")
def patch_by_id(id: uuid.UUID, question: QuestionCategoryMapBaseModelCreateById, db: Session = Depends(get_db)):
    """Patch by Id"""
    query_obj = db.query(QuestionCategoryMapBase).where(QuestionCategoryMapBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(QuestionCategoryMapBase).where(QuestionCategoryMapBase.id == id).update(question.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.delete("/")
def delete_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Delete by Id"""
    query_obj = db.query(QuestionCategoryMapBase).where(QuestionCategoryMapBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(QuestionCategoryMapBase).where(QuestionCategoryMapBase.id == id).delete()
        db.commit()
    db.close()
    return {"message": "success"}


@router.get("/all")
def get_all(db: Session = Depends(get_db)):
    """Get all data"""
    return db.query(QuestionCategoryMapBase).all()


@router.get("/findByLive")
def is_live(live=True, db: Session = Depends(get_db)):
    """Get live status"""
    return db.query(QuestionCategoryMapBase).filter(QuestionCategoryMapBase.live == live).all()
