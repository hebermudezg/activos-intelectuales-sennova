from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from jose import JWTError, jwt
from .auth import router as auth_router, get_current_user
from .usuarios import router as usuarios_router
from .productos import router as productos_router
from .programas import router as programas_router
from .proyectos import router as proyectos_router
from ..db.database import init_db, get_db
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


SECRET_KEY = "your_secret_key"
ALGORITHM = "HS256"
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")

templates = Jinja2Templates(directory="src/templates")

app.include_router(auth_router, prefix="/auth", tags=["Auth"])
app.include_router(usuarios_router, prefix="/usuarios", tags=["Usuarios"])
app.include_router(productos_router, prefix="/productos", tags=["Productos"])
app.include_router(programas_router, prefix="/programas", tags=["Programas"])
app.include_router(proyectos_router, prefix="/proyectos", tags=["Proyectos"])

async def get_current_user_from_cookie(request: Request, db: Session = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )

    token = request.cookies.get("access_token")
    if not token:
        raise HTTPException(status_code=401, detail="Not authenticated")
    try:
        payload = jwt.decode(token.split(" ")[1], SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception
    user = db.query(models.Usuario).filter(models.Usuario.correo_electronico == username).first()
    if user is None:
        raise credentials_exception
    return user


@app.get("/", response_class=HTMLResponse, tags=["General"])
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/dashboard", response_class=HTMLResponse, tags=["General"])
async def dashboard(request: Request, user: models.Usuario = Depends(get_current_user_from_cookie)):
    return templates.TemplateResponse("dashboard.html", {"request": request, "user": user})

@app.get("/auth/login", response_class=HTMLResponse, tags=["Auth"])
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})



if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.api.main:app", host="127.0.0.1", port=8000, log_level="info")