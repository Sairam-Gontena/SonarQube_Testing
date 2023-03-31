""" patient questionnaire controller """
import datetime
import uuid

# session is automatically closed with the URL associated with it at the end of block
from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.patient_questionnaire import PatientQuestionnaireBaseModelCreateById, PatientQuestionnaireBase
from config.database_connection import get_db

router = APIRouter()


@router.get("/")
def get_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Get By id"""
    query_obj = db.query(PatientQuestionnaireBase).filter(PatientQuestionnaireBase.id == id).all()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        return query_obj


@router.post("/")
def post_all(patient_questionnaire: PatientQuestionnaireBaseModelCreateById, db: Session = Depends(get_db)):
    """Post ALL Data"""
    post_data = PatientQuestionnaireBase(patient_id=patient_questionnaire.patient_id,
                                         category_id=patient_questionnaire.category_id,
                                         response_json=patient_questionnaire.response_json,
                                         modified_on=datetime.datetime.utcnow(),
                                         modified_by=patient_questionnaire.modified_by,
                                         live=patient_questionnaire.live,
                                         version=patient_questionnaire.version)
    db.add(post_data)
    try:
        db.commit()
    except IntegrityError as e:
        raise HTTPException(status_code=422, detail=f"{e.orig}")
    db.close()
    return {"message": "success"}


@router.put("/")
def update_by_id(id: uuid.UUID, patient_questionnaire: PatientQuestionnaireBaseModelCreateById,
                 db: Session = Depends(get_db)):
    """Update by id"""
    query_obj = db.query(PatientQuestionnaireBase).where(PatientQuestionnaireBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        patient_questionnaire.dict().update({"modified_on": f"{datetime.datetime.utcnow()}"})
        db.query(PatientQuestionnaireBase).where(PatientQuestionnaireBase.id == id).update(patient_questionnaire.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.patch("/")
def patch_by_id(id: uuid.UUID, patient_questionnaire: PatientQuestionnaireBaseModelCreateById,
                db: Session = Depends(get_db)):
    """Patch by id"""
    query_obj = db.query(PatientQuestionnaireBase).where(PatientQuestionnaireBase.id == id).first()
    if not query_obj:
        print("Id does not exist")
        return {"message": "Id does not exist"}
    else:
        db.query(PatientQuestionnaireBase).where(PatientQuestionnaireBase.id == id).update(patient_questionnaire.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.delete("/")
def delete_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Delete by id"""
    query_obj = db.query(PatientQuestionnaireBase).where(PatientQuestionnaireBase.id == id).first()
    if not query_obj:
        print("Id does not exist")
        return {"message": "Id does not exist"}
    else:
        db.query(PatientQuestionnaireBase).where(PatientQuestionnaireBase.id == id).delete()
        db.commit()
    db.close()
    return {"message": "success"}


@router.get("/all")
def get_all(db: Session = Depends(get_db)):
    """Get all data"""
    return db.query(PatientQuestionnaireBase).all()


@router.get("/findByLive")
def is_live(live=True, db: Session = Depends(get_db)):
    """Get live status"""
    return db.query(PatientQuestionnaireBase).filter(PatientQuestionnaireBase.live == live).all()
