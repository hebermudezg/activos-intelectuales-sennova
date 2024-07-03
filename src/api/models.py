from pydantic import BaseModel
from typing import Optional
from datetime import date

class UsuarioCreate(BaseModel):
    id_usuario: int
    nombre_completo: str
    correo_electronico: str
    telefono: str
    rol: str
    password: str

class ProductoCreate(BaseModel):
    id: int
    categoria: str
    nombre_del_producto: str
    producto_terminado: bool

class ProgramaCreate(BaseModel):
    id: int
    nombre_del_programa: str
    tipo: str

class Programa(BaseModel):
    id: int
    nombre_del_programa: str
    tipo: str

class ProyectoCreate(BaseModel):
    id_proyecto: int
    titulo: str
    fecha_inicio: date
    fecha_fin: date
    entidad_financia: str
    codigo_sgp: Optional[str] = None
    valor: int
    linea_programatica: str
    resumen: str

class Proyecto(BaseModel):
    id_proyecto: int
    titulo: str
    fecha_inicio: date
    fecha_fin: date
    entidad_financia: str
    codigo_sgp: Optional[str] = None
    valor: int
    linea_programatica: str
    resumen: str

class Token(BaseModel):
    access_token: str
    token_type: str
