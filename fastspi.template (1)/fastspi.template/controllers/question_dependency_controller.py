""" question dependency controller """
import datetime
import uuid

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.question_dependency import QuestionDependencyBaseModelCreateById, QuestionDependencyBase
from config.database_connection import get_db

router = APIRouter()


@router.get("/")
def get_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Get By id"""
    query_obj = db.query(QuestionDependencyBase).filter(QuestionDependencyBase.id == id).all()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        return query_obj


@router.post("/")
def post_all(question_dependency: QuestionDependencyBaseModelCreateById, db: Session = Depends(get_db)):
    """Post ALL Data"""
    post_data = QuestionDependencyBase(question_id=question_dependency.question_id,
                                       dependent_question_id=question_dependency.dependent_question_id,
                                       modified_on=datetime.datetime.utcnow(),
                                       modified_by=question_dependency.modified_by,
                                       live=question_dependency.live,
                                       version=question_dependency.version)
    db.add(post_data)
    try:
        db.commit()
    except IntegrityError as e:
        raise HTTPException(status_code=422, detail=f"{e.orig}") from e
    db.close()
    return {"message": "success"}


@router.put("/")
def update_by_id(id: uuid.UUID, question_dependency: QuestionDependencyBaseModelCreateById,
                 db: Session = Depends(get_db)):
    """Update by Id"""
    query_obj = db.query(QuestionDependencyBase).where(QuestionDependencyBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        question_dependency.dict().update({"modified_on": f"{datetime.datetime.utcnow()}"})
        db.query(QuestionDependencyBase).where(QuestionDependencyBase.id == id).update(
            question_dependency.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.patch("/")
def patch_by_id(id: uuid.UUID, question_dependency: QuestionDependencyBaseModelCreateById,
                db: Session = Depends(get_db)):
    """Patch by Id"""
    query_obj = db.query(QuestionDependencyBase).where(QuestionDependencyBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(QuestionDependencyBase).where(QuestionDependencyBase.id == id).update(
            question_dependency.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.delete("/")
def delete_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Delete by Id"""
    query_obj = db.query(QuestionDependencyBase).where(QuestionDependencyBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(QuestionDependencyBase).where(QuestionDependencyBase.id == id).delete()
        db.commit()
    db.close()
    return {"message": "success"}


@router.get("/all")
def get_all(db: Session = Depends(get_db)):
    """Get all data"""
    return db.query(QuestionDependencyBase).all()


@router.get("/findByLive")
def is_live(live=True, db: Session = Depends(get_db)):
    """Get live status"""
    return db.query(QuestionDependencyBase).filter(QuestionDependencyBase.live == live).all()
