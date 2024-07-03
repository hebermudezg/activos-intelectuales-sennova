from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import models
from ..db.database import get_db
from .auth import get_current_user
from .models import ProgramaCreate, Programa, UsuarioCreate

router = APIRouter()

@router.post("/", response_model=Programa)
def create_programa(programa: ProgramaCreate, db: Session = Depends(get_db), current_user: UsuarioCreate = Depends(get_current_user)):
    db_programa = models.Programa(**programa.dict())
    db.add(db_programa)
    db.commit()
    db.refresh(db_programa)
    return db_programa

@router.get("/{id}", response_model=Programa)
def read_programa(id: int, db: Session = Depends(get_db), current_user: UsuarioCreate = Depends(get_current_user)):
    db_programa = db.query(models.Programa).filter(models.Programa.id == id).first()
    if db_programa is None:
        raise HTTPException(status_code=404, detail="Programa not found")
    return db_programa

@router.put("/{id}", response_model=Programa)
def update_programa(id: int, programa: ProgramaCreate, db: Session = Depends(get_db), current_user: UsuarioCreate = Depends(get_current_user)):
    db_programa = db.query(models.Programa).filter(models.Programa.id == id).first()
    if db_programa is None:
        raise HTTPException(status_code=404, detail="Programa not found")
    for key, value in programa.dict().items():
        setattr(db_programa, key, value)
    db.commit()
    db.refresh(db_programa)
    return db_programa

@router.delete("/{id}")
def delete_programa(id: int, db: Session = Depends(get_db), current_user: UsuarioCreate = Depends(get_current_user)):
    db_programa = db.query(models.Programa).filter(models.Programa.id == id).first()
    if db_programa is None:
        raise HTTPException(status_code=404, detail="Programa not found")
    db.delete(db_programa)
    db.commit()
    return {"message": "Programa deleted successfully"}
