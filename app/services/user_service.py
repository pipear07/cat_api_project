# Importo la base de datos desde donde me conecto a Mongo
from app.db.mongo import db

# Importo el modelo de entrada para los datos del usuario
from app.models.user_model import UserIn

# Importo hashlib para poder encriptar la contraseña con SHA256
import hashlib

# Esta funcion genera el username automáticamente a partir del nombre y apellido
# Lo convierte todo en minúscula y los junta con un punto (ej: juan.perez)
def generate_username(first: str, last: str) -> str:
    return (first + "." + last).lower()

# Esta funcion se encarga de crear un nuevo usuario en la base de datos
async def create_user(user: UserIn):
    username = generate_username(user.first_name, user.last_name)  # genero el username
    existing = await db.users.find_one({"username": username})  # reviso si ya existe ese username
    if existing:
        return None  # si ya existe, devuelvo None para que el controlador maneje eso
    user_data = {
        "username": username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        # encripto la contraseña con SHA256 para no guardarla en texto plano
        "password": hashlib.sha256(user.password.encode()).hexdigest()
    }
    # guardo el usuario en la colección "users"
    await db.users.insert_one(user_data)
    return user_data  # retorno el usuario que acabo de crear

# Esta funcion lista los usuarios, pero solo los primeros 50 por si hay muchos
async def list_users():
    return await db.users.find().to_list(50)

# Esta funcion sirve para hacer login, comparando el username y la contraseña encriptada
async def login(username: str, password: str):
    hashed = hashlib.sha256(password.encode()).hexdigest()  # encripto la contraseña igual que cuando se guardo
    # busco si existe un usuario con ese username y esa contraseña
    user = await db.users.find_one({"username": username, "password": hashed})
    return user  # si lo encuentra, lo devuelve, si no, devuelve None
