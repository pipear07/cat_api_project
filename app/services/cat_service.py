# Importo httpx que es la librera que uso para hacer peticiones HTTP de forma asincrona
import httpx

# Importo el modelo que definí para las razas de gatos, aunque aqui en realidad no lo estoy usando directamente
from app.models.cat_model import CatBreed

# Esta es la API key que uso para conectarme a TheCatAPI (es publica para la prueba)
API_KEY = "live_JBT0Ah0Nt12iyl2IpjQVLDWjcLk0GQwf4zI9wBMfmfejKmcC31mOJp4yJz5TsOUP"

# La URL base de la API externa de gatos
BASE_URL = "https://api.thecatapi.com/v1"

# Aqui guardo los headers que necesito enviar en cada peticion para autenticarme con la API
HEADERS = {
    "x-api-key": API_KEY
}

# Esta funcion se conecta a la API y me devuelve todas las razas de gatos
async def get_all_breeds():
    # Uso httpx para hacer la solicitud GET a la ruta /breeds
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{BASE_URL}/breeds", headers=HEADERS)
        return response.json()  # devuelvo la respuesta en formato JSON

# Esta funcion busca una raza específica por su ID (yo la uso cuando llaman /breeds/{breed_id})
async def get_breed_by_id(breed_id: str):
    breeds = await get_all_breeds()  # primero traigo todas las razas
    for breed in breeds:
        if breed["id"] == breed_id:  # reviso si alguna tiene el ID que me pasaron
            return breed  # si la encuentro, la devuelvo
    return None  # si no hay ninguna con ese ID, devuelvo None

# Esta funcion busca razas por nombre (se usa cuando llaman /breeds/search?name=...)
async def search_breeds(query: str):
    async with httpx.AsyncClient() as client:
        # hago una peticion GET a la ruta de busqueda pasandole el nombre como query param
        response = await client.get(f"{BASE_URL}/breeds/search?q={query}", headers=HEADERS)
        return response.json()  # devuelvo el resultado tal cual en JSON
