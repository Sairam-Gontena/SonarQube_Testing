""" questionnaire template controller """
import datetime
import uuid

# session is automatically closed with the URL associated with it at the end of block
from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.questionnaire_template import QuestionnaireTemplateBaseModelCreateById, QuestionnaireTemplateBase
from config.database_connection import get_db

router = APIRouter()


@router.get("/")
def get_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Get By id"""
    query_obj = db.query(QuestionnaireTemplateBase).filter(QuestionnaireTemplateBase.id == id).all()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        return query_obj


@router.post("/")
def post_all(questionnaire_template: QuestionnaireTemplateBaseModelCreateById, db: Session = Depends(get_db)):
    """Post ALL Data"""
    post_data = QuestionnaireTemplateBase(id=uuid.uuid4(),
                                          category_id=questionnaire_template.category_id,
                                          questionnaire_json=questionnaire_template.questionnaire_json,
                                          modified_on=datetime.datetime.utcnow(),
                                          modified_by=questionnaire_template.modified_by,
                                          live=questionnaire_template.live,
                                          version=questionnaire_template.version)
    db.add(post_data)
    try:
        db.commit()
    except IntegrityError as e:
        raise HTTPException(status_code=422, detail=f"{e.orig}")
    db.close()
    return {"message": "success"}


@router.put("/")
def update_by_id(id: uuid.UUID, questionnaire_template: QuestionnaireTemplateBaseModelCreateById,
                 db: Session = Depends(get_db)):
    """Update by id"""
    query_obj = db.query(QuestionnaireTemplateBase).where(QuestionnaireTemplateBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        questionnaire_template.dict().update({"modified_on": f"{datetime.datetime.utcnow()}"})
        db.query(QuestionnaireTemplateBase).where(QuestionnaireTemplateBase.id == id).update(
            questionnaire_template.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.patch("/")
def patch_by_id(id: uuid.UUID, questionnaire_template: QuestionnaireTemplateBaseModelCreateById,
                db: Session = Depends(get_db)):
    """Patch by id"""
    query_obj = db.query(QuestionnaireTemplateBase).where(QuestionnaireTemplateBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(QuestionnaireTemplateBase).where(QuestionnaireTemplateBase.id == id).update(
            questionnaire_template.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.delete("/")
def delete_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Delete by Id"""
    query_obj = db.query(QuestionnaireTemplateBase).where(QuestionnaireTemplateBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(QuestionnaireTemplateBase).where(QuestionnaireTemplateBase.id == id).delete()
        db.commit()
    db.close()
    return {"message": "success"}


@router.get("/all")
def get_all(db: Session = Depends(get_db)):
    """Get all data"""
    return db.query(QuestionnaireTemplateBase).all()


@router.get("/findByLive")
def is_live(live=True, db: Session = Depends(get_db)):
    """Get live status"""
    return db.query(QuestionnaireTemplateBase).filter(QuestionnaireTemplateBase.live == live).all()
