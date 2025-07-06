# Importo BaseModel de Pydantic; esto me ayuda a validar y estructurar datos de forma chévere
from pydantic import BaseModel

# Defino la clase que representa una raza de gato (lo que espero recibir / enviar)
class CatBreed(BaseModel):
    id: str                      # el id que viene de TheCatAPI, lo guardo como string
    name: str                    # nombre de la raza
    origin: str | None = None    # de dOnde es la raza, puede venir vacío, por eso lo pongo opcional
    description: str | None = None  # descripciOn breve, también opcional porque a veces no la devuelven
