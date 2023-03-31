""" category map controller """
import datetime
import uuid

# session is automatically closed with the URL associated with it at the end of block
from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from models.category_map import CategoryMapBaseModelCreateById, CategoryMapBase
from config.database_connection import get_db

router = APIRouter()


@router.get("/")
def get_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Get By id"""
    query_obj = db.query(CategoryMapBase).filter(CategoryMapBase.id == id).all()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        return query_obj


@router.post("/")
def post_all(category_map: CategoryMapBaseModelCreateById, db: Session = Depends(get_db)):
    """Post ALL Data"""
    post_data = CategoryMapBase(category_id=category_map.category_id,
                                parent_category_id=category_map.parent_category_id,
                                sequence=category_map.sequence,
                                modified_on=datetime.datetime.utcnow(),
                                modified_by=category_map.modified_by,
                                live=category_map.live,
                                version=category_map.version)
    db.add(post_data)
    try:
        db.commit()
    except IntegrityError as e:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail=f"{e.orig}") from e
    db.close()
    return {"message": "success"}


@router.put("/")
def update_by_id(id: uuid.UUID, category_map: CategoryMapBaseModelCreateById, db: Session = Depends(get_db)):
    """Update by id"""
    query_obj = db.query(CategoryMapBase).where(CategoryMapBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(CategoryMapBase).where(CategoryMapBase.id == id).update(category_map.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.patch("/")
def patch_by_id(id: uuid.UUID, category_map: CategoryMapBaseModelCreateById, db: Session = Depends(get_db)):
    """Patch by Id"""
    query_obj = db.query(CategoryMapBase).where(CategoryMapBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(CategoryMapBase).where(CategoryMapBase.id == id).update(category_map.dict())
        db.commit()
    db.close()
    return {"message": "success"}


@router.delete("/")
def delete_by_id(id: uuid.UUID, db: Session = Depends(get_db)):
    """Delete by Id"""
    query_obj = db.query(CategoryMapBase).where(CategoryMapBase.id == id).first()
    if not query_obj:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Id does not exist")
    else:
        db.query(CategoryMapBase).where(CategoryMapBase.id == id).delete()
        db.commit()
    db.close()
    return {"message": "success"}


@router.get("/all")
def get_all(db: Session = Depends(get_db)):
    """Get all data"""
    return db.query(CategoryMapBase).all()


@router.get("/findByLive")
def is_live(live=True, db: Session = Depends(get_db)):
    """Get live status"""
    return db.query(CategoryMapBase).filter(CategoryMapBase.live == live).all()
