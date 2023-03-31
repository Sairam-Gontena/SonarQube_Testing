""" category controller """
import datetime
import uuid

from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.category import CategoryBaseModelCreateById, CategoryBase
from config.database_connection import get_db

router = APIRouter()


@router.get("/")
def get_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Get By id"""
    query_obj = db.query(CategoryBase).filter(CategoryBase.id == id).all()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        return query_obj


@router.post("/")
def post_all(category: CategoryBaseModelCreateById, db: Session = Depends(get_db)):
    """Post ALL Data"""
    post_data = CategoryBase(category_sid=category.category_sid,
                             category_name=category.category_name,
                             modified_on=datetime.datetime.utcnow(),
                             modified_by=category.modified_by,
                             live=category.live,
                             version=category.version)
    db.add(post_data)
    try:
        db.commit()
    except IntegrityError as e:
        raise HTTPException(status_code=422, detail=f"{e.orig}") from e
    db.close()
    return {"message": "success"}


@router.put("/")
def update_by_id(id: uuid.UUID, category: CategoryBaseModelCreateById,
                 db: Session = Depends(get_db)):
    """Update by id"""
    query_obj = db.query(CategoryBase).where(CategoryBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        category.dict().update({"modified_on": f"{datetime.datetime.utcnow()}"})
        db.query(CategoryBase).where(CategoryBase.id == id).update(category.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.patch("/")
def patch_by_id(id: uuid.UUID, category: CategoryBaseModelCreateById,
                db: Session = Depends(get_db)):
    """Patch by id"""
    query_obj = db.query(CategoryBase).where(CategoryBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(CategoryBase).where(CategoryBase.id == id).update(category.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.delete("/")
def delete_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Delete by id"""
    query_obj = db.query(CategoryBase).where(CategoryBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(CategoryBase).where(CategoryBase.id == id).delete()
        db.commit()
    db.close()
    return {"message": "success"}


@router.get("/all")
def get_all(db: Session = Depends(get_db)):
    """Get all data as a list"""
    return db.query(CategoryBase).all()


@router.get("/findByLive")
def is_live(live=True, db: Session = Depends(get_db)):
    """Get live status"""
    return db.query(CategoryBase).filter(CategoryBase.live == live).all()
