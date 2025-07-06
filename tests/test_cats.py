import sys
import os
# Estas lineas las puse porque si ejecuto pytest directamente, a veces no encuentra el modulo 'app'
# Lo que hago es agregar manualmente al sys.path el directorio raiz del proyecto (que está un nivel arriba)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Importo el cliente de pruebas y la app
from fastapi.testclient import TestClient
from app.main import app

# Creo el cliente para hacer las pruebas
client = TestClient(app)

# Esta función prueba que el endpoint de razas funcione
def test_get_breeds():
    res = client.get("/cats/breeds")
    assert res.status_code == 200

# Esta función prueba buscar una raza que probablemente no exista
def test_get_unknown_breed():
    res = client.get("/cats/breeds/xyz")
    assert res.status_code in [404, 200]
