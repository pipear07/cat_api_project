# Importo la librería motor que me permite conectarme a MongoDB de forma asíncrona
from motor.motor_asyncio import AsyncIOMotorClient

# Importo os para poder leer las variables de entorno, como la URL de conexión a la base
import os

# Aquí saco la URL de conexión de una variable de entorno llamada MONGO_URL,
# y si no existe, uso una por defecto que es localhost
MONGO_URL = os.getenv("MONGO_URL", "mongodb://localhost:27017")

# Creo el cliente para conectarme a Mongo usando esa URL
client = AsyncIOMotorClient(MONGO_URL)

# Finalmente, selecciono la base de datos que voy a usar, en este caso le puse "cat_user_db"
db = client["cat_user_db"]
