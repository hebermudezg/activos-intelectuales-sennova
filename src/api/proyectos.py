from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import models
from ..db.database import get_db
from .auth import get_current_user
from .models import ProyectoCreate, Proyecto, UsuarioCreate

router = APIRouter()

@router.post("/", response_model=Proyecto)
def create_proyecto(proyecto: ProyectoCreate, db: Session = Depends(get_db), current_user: UsuarioCreate = Depends(get_current_user)):
    db_proyecto = models.Proyecto(**proyecto.dict())
    db.add(db_proyecto)
    db.commit()
    db.refresh(db_proyecto)
    return db_proyecto

@router.get("/{id}", response_model=Proyecto)
def read_proyecto(id: int, db: Session = Depends(get_db), current_user: UsuarioCreate = Depends(get_current_user)):
    db_proyecto = db.query(models.Proyecto).filter(models.Proyecto.id_proyecto == id).first()
    if db_proyecto is None:
        raise HTTPException(status_code=404, detail="Proyecto not found")
    return db_proyecto

@router.put("/{id}", response_model=Proyecto)
def update_proyecto(id: int, proyecto: ProyectoCreate, db: Session = Depends(get_db), current_user: UsuarioCreate = Depends(get_current_user)):
    db_proyecto = db.query(models.Proyecto).filter(models.Proyecto.id_proyecto == id).first()
    if db_proyecto is None:
        raise HTTPException(status_code=404, detail="Proyecto not found")
    for key, value in proyecto.dict().items():
        setattr(db_proyecto, key, value)
    db.commit()
    db.refresh(db_proyecto)
    return db_proyecto

@router.delete("/{id}")
def delete_proyecto(id: int, db: Session = Depends(get_db), current_user: UsuarioCreate = Depends(get_current_user)):
    db_proyecto = db.query(models.Proyecto).filter(models.Proyecto.id_proyecto == id).first()
    if db_proyecto is None:
        raise HTTPException(status_code=404, detail="Proyecto not found")
    db.delete(db_proyecto)
    db.commit()
    return {"message": "Proyecto deleted successfully"}
