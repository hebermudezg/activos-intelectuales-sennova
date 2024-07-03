from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Tabla de asociación para la relación muchos a muchos entre Proyecto y Programa
proyecto_programa = Table('proyecto_programa', Base.metadata,
    Column('proyecto_id', Integer, ForeignKey('proyecto.id_proyecto'), primary_key=True),
    Column('programa_id', Integer, ForeignKey('programa.id'), primary_key=True)
)

class Usuario(Base):
    __tablename__ = 'usuario'
    id_usuario = Column(Integer, primary_key=True)
    nombre_completo = Column(String, nullable=False)
    correo_electronico = Column(String, nullable=False, unique=True)
    telefono = Column(String, nullable=False)
    rol = Column(String, nullable=False)
    password = Column(String, nullable=False)


class Producto(Base):
    __tablename__ = 'producto'
    id = Column(Integer, primary_key=True)
    categoria = Column(String, nullable=False)  # Ejemplos: Artículo, Libro, Informe, Software
    nombre_del_producto = Column(String, nullable=False)
    producto_terminado = Column(Boolean, nullable=False)

class Proyecto(Base):
    __tablename__ = 'proyecto'
    id_proyecto = Column(Integer, primary_key=True)
    titulo = Column(String, nullable=False)
    fecha_inicio = Column(DateTime, nullable=False)
    fecha_fin = Column(DateTime, nullable=False)
    entidad_financia = Column(String, nullable=False)  # Ejemplos: SENNOVA, XXX
    codigo_sgp = Column(String, nullable=True)  # Null si no aplica
    valor = Column(Integer, nullable=False)
    linea_programatica = Column(String, nullable=False)  # 5 opciones
    resumen = Column(String, nullable=False)

    # Relaciones
    programas = relationship("Programa", secondary=proyecto_programa, back_populates="proyectos")

class Programa(Base):
    __tablename__ = 'programa'
    id = Column(Integer, primary_key=True)
    nombre_del_programa = Column(String, nullable=False)
    tipo = Column(String, nullable=False)  # Ejemplos: Técnico, Tecnológico

    # Relaciones
    proyectos = relationship("Proyecto", secondary=proyecto_programa, back_populates="programas")
