# Importo BaseModel de Pydantic para poder validar los datos que entran o salen
from pydantic import BaseModel

# Este modelo lo uso cuando me mandan datos para crear un usuario
class UserIn(BaseModel):
    first_name: str   # nombre del usuario
    last_name: str    # apellido del usuario
    password: str     # contraseña que se guarda (despues la encripto)

# Este otro modelo lo uso cuando devuelvo datos de un usuario (sin incluir la contraseña)
class UserOut(BaseModel):
    username: str     # el username que genero automáticamente
    first_name: str   # nombre
    last_name: str    # apellido
