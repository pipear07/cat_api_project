# Importo FastAPI para crear la aplicacion principal
from fastapi import FastAPI

# Importo los routers que ya hice para gatos y usuarios
from app.controllers.cat_controller import router as cat_router
from app.controllers.user_controller import router as user_router

# Creo la instancia principal de FastAPI, que es la app que se va a levantar
app = FastAPI()

# Le agrego el router de gatos con el prefijo /cats para que todos los endpoints queden organizados
app.include_router(cat_router, prefix="/cats", tags=["Cats"])

# Agrego el router de usuarios con el prefijo /users para lo mismo
app.include_router(user_router, prefix="/users", tags=["Users"])

# Este es el endpoint raiz que solo muestra un mensaje para saber que la API esta viva
@app.get("/")
def read_root():
    return {"message": "API de gatos y usuarios lista "}
