from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ..db import models
from ..db.database import get_db
from .auth import get_current_user
from .models import ProductoCreate, UsuarioCreate

router = APIRouter()

@router.post("/", response_model=ProductoCreate)
def create_producto(producto: ProductoCreate, db: Session = Depends(get_db), current_user: UsuarioCreate = Depends(get_current_user)):
    db_producto = models.Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@router.get("/{id}", response_model=ProductoCreate)
def read_producto(id: int, db: Session = Depends(get_db), current_user: UsuarioCreate = Depends(get_current_user)):
    db_producto = db.query(models.Producto).filter(models.Producto.id == id).first()
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    return db_producto

@router.put("/{id}", response_model=ProductoCreate)
def update_producto(id: int, producto: ProductoCreate, db: Session = Depends(get_db), current_user: UsuarioCreate = Depends(get_current_user)):
    db_producto = db.query(models.Producto).filter(models.Producto.id == id).first()
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    for key, value in producto.dict().items():
        setattr(db_producto, key, value)
    db.commit()
    db.refresh(db_producto)
    return db_producto

@router.delete("/{id}")
def delete_producto(id: int, db: Session = Depends(get_db), current_user: UsuarioCreate = Depends(get_current_user)):
    db_producto = db.query(models.Producto).filter(models.Producto.id == id).first()
    if db_producto is None:
        raise HTTPException(status_code=404, detail="Producto not found")
    db.delete(db_producto)
    db.commit()
    return {"message": "Producto deleted successfully"}
