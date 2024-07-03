from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer
from .usuarios import router as usuarios_router
from .productos import router as productos_router
from .programas import router as programas_router
from .proyectos import router as proyectos_router
from .auth import router as auth_router, get_current_user
from ..db.database import engine
from ..db import models
from .models import UsuarioCreate

# Automatically create database tables based on SQLAlchemy models at startup.
models.Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="API con Autenticación",
    description="Esta es una API con autenticación usando OAuth2",
    version="1.0.0",
    openapi_tags=[
        {"name": "Auth", "description": "Rutas de autenticación"},
        {"name": "Usuarios", "description": "Operaciones con usuarios"},
        {"name": "Productos", "description": "Operaciones con productos"},
        {"name": "Programas", "description": "Operaciones con programas"},
        {"name": "Proyectos", "description": "Operaciones con proyectos"}
    ],
)

# Templates
templates = Jinja2Templates(directory="src/templates")

# Include routers from different modules
app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(usuarios_router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(productos_router, prefix="/productos", tags=["Productos"])
app.include_router(programas_router, prefix="/programas", tags=["Programas"])
app.include_router(proyectos_router, prefix="/proyectos", tags=["Proyectos"])

@app.get("/", response_class=HTMLResponse, tags=["General"])
async def read_root(request: Request, user: UsuarioCreate = Depends(get_current_user)):
    return templates.TemplateResponse("index.html", {"request": request, "user": user})

# Define more routers or additional configurations if needed
