# Importo lo necesario de FastAPI: el enrutador y para lanzar errores si algo sale mal
from fastapi import APIRouter, HTTPException

# Traigo los modelos que definí para la entrada (UserIn) y la salida (UserOut) de los datos
from app.models.user_model import UserIn, UserOut

# Traigo las funciones del servicio que creé: para crear usuarios, listar y hacer login
from app.services.user_service import create_user, list_users, login

# Creo el router específico para los endpoints de usuarios
router = APIRouter()

# Este endpoint simplemente me devuelve la lista de usuarios que hay guardados en la base
@router.get("/", response_model=list[UserOut])
async def get_users():
    return await list_users()  # llamo a la función que consulta en MongoDB y devuelvo la lista

# Este endpoint se usa para crear un nuevo usuario, validando que el username no se repita
@router.post("/", response_model=UserOut)
async def post_user(user: UserIn):
    created = await create_user(user)  # llamo a la función del servicio que se encarga de guardarlo
    if not created:
        # si la función devuelve None, significa que ya existía el username, entonces lanzo un error 400
        raise HTTPException(status_code=400, detail="Username duplicado")
    return created  # si se creó bien, lo devuelvo tal cual

# Este endpoint sirve para loguearse, recibe el username y la contraseña como parámetros
@router.get("/login")
async def get_login(username: str, password: str):
    user = await login(username, password)  # llamo a la función que verifica si existen en la base
    if not user:
        # si no hay coincidencia, devuelvo un error 401 de credenciales incorrectas
        raise HTTPException(status_code=401, detail="Credenciales inválidas")
    return user  # si todo bien, devuelvo los datos del usuario
