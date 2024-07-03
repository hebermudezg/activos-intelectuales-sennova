from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import models
from ..db.database import get_db
from .auth import get_current_user
from .models import UsuarioCreate

router = APIRouter()

@router.post("/", response_model=UsuarioCreate)
def create_usuario(usuario: UsuarioCreate, db: Session = Depends(get_db), current_user: UsuarioCreate = Depends(get_current_user)):
    db_usuario = models.Usuario(**usuario.dict())
    db.add(db_usuario)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@router.get("/{id_usuario}", response_model=UsuarioCreate)
def read_usuario(id_usuario: int, db: Session = Depends(get_db), current_user: UsuarioCreate = Depends(get_current_user)):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == id_usuario).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    return db_usuario

@router.put("/{id_usuario}", response_model=UsuarioCreate)
def update_usuario(id_usuario: int, usuario: UsuarioCreate, db: Session = Depends(get_db), current_user: UsuarioCreate = Depends(get_current_user)):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == id_usuario).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    for key, value in usuario.dict().items():
        setattr(db_usuario, key, value)
    db.commit()
    db.refresh(db_usuario)
    return db_usuario

@router.delete("/{id_usuario}")
def delete_usuario(id_usuario: int, db: Session = Depends(get_db), current_user: UsuarioCreate = Depends(get_current_user)):
    db_usuario = db.query(models.Usuario).filter(models.Usuario.id_usuario == id_usuario).first()
    if db_usuario is None:
        raise HTTPException(status_code=404, detail="Usuario not found")
    db.delete(db_usuario)
    db.commit()
    return {"message": "Usuario deleted successfully"}
