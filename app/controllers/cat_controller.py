# Importo cosas de FastAPI que necesito: el enrutador, excepciones y para manejar parámetros de query
from fastapi import APIRouter, HTTPException, Query

# Traigo los métodos que hice en el servicio de gatos para usarlos aquí
from app.services.cat_service import get_all_breeds, get_breed_by_id, search_breeds

# Creo el router para agrupar los endpoints relacionados a gatos
router = APIRouter()

# Este endpoint lista todas las razas de gatos, lo que hago es llamar al servicio que ya consulta la API externa
@router.get("/breeds")
async def list_breeds():
    return await get_all_breeds()

# Este endpoint devuelve una sola raza, según el id que le paso por la URL
@router.get("/breeds/{breed_id}")
async def get_breed(breed_id: str):
    breed = await get_breed_by_id(breed_id)  # llamo al servicio pasando el id
    if not breed:
        # si no encuentra nada, lanzo error 404 con un mensaje
        raise HTTPException(status_code=404, detail="Raza no encontrada")
    return breed  # si sí la encontró, la retorno

# Este endpoint busca razas por nombre (o parte del nombre), lo que hago es usar un parámetro llamado name
@router.get("/breeds/search")
async def search_breed(name: str = Query(..., description="Nombre parcial de la raza")):
    results = await search_breeds(name)  # llamo al servicio con el nombre como parámetro
    if not results:
        # si no encuentra ninguna coincidencia, devuelvo error 404 también
        raise HTTPException(status_code=404, detail="No se encontraron coincidencias")
    return results  # si hay resultados, los devuelvo como están
