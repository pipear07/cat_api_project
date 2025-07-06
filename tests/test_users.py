import sys
import os
# Estas lineas las puse porque si ejecuto pytest directamente, a veces no encuentra el modulo 'app'
# Lo que hago es agregar manualmente al sys.path el directorio raiz del proyecto (que está un nivel arriba)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importo TestClient que me permite probar la API como si fuera un cliente externo
from fastapi.testclient import TestClient

# Importo la app principal para poder probarla directamente
from app.main import app

# Creo el cliente de pruebas a partir de la app
client = TestClient(app)

# Esta prueba revisa que el endpoint raíz (/) responda correctamente
def test_root():
    res = client.get("/")              # hago una petición GET al endpoint raíz
    assert res.status_code == 200     # verifico que la respuesta tenga código 200 (OK)

# Esta prueba revisa que el endpoint para listar usuarios funcione sin errores
def test_get_users():
    res = client.get("/users/")       # hago una petición GET a /users/
    assert res.status_code == 200     # espero que devuelva 200 si todo está bien
