from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from .auth import router as auth_router, get_current_user
from .usuarios import router as usuarios_router
from .productos import router as productos_router
from .programas import router as programas_router
from .proyectos import router as proyectos_router
from ..db.database import init_db
from ..db import models

# Inicializar la base de datos
init_db()

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

templates = Jinja2Templates(directory="src/templates")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(usuarios_router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(productos_router, prefix="/productos", tags=["Productos"])
app.include_router(programas_router, prefix="/programas", tags=["Programas"])
app.include_router(proyectos_router, prefix="/proyectos", tags=["Proyectos"])

@app.get("/", response_class=HTMLResponse, tags=["General"])
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse, tags=["General"])
async def dashboard(request: Request, user: models.Usuario = Depends(get_current_user)):
    return templates.TemplateResponse("dashboard.html", {"request": request, "user": user})

@app.get("/auth/login", response_class=HTMLResponse, tags=["Auth"])
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.get("/auth/register", response_class=HTMLResponse, tags=["Auth"])
async def register(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})
