# API de Gatos y Usuarios

Este proyecto es una API construida con FastAPI y MongoDB que se conecta a [TheCatAPI](https://thecatapi.com/) para obtener información de razas de gatos, y también permite registrar y autenticar usuarios.

---

### Usuarios
- `GET /users/`
- `POST /users/`
- `GET /users/login?username=...&password=...`

### Gatos
- `GET /cats/breeds`
- `GET /cats/breeds/{breed_id}`
- `GET /cats/breeds/search?name=...`

## Docker

```bash
docker build -t cat-api .
docker run -p 8000:8000 cat-api
```

### 1. Crea y activa un entorno virtual


```bash
python -m venv venv
.\venv\Scripts activate
```


### 2. Instala las dependencias

```bash
pip install -r requirements.txt
```

### 3. Crea tu archivo .env

Copia el archivo `.env.example` y renómbralo como `.env` si quiereN personalizarlo.

```env
MONGO_URL=mongodb://localhost:27017
```

### 4. Ejecuta el servidor

```bash
uvicorn app.main:app --reload
```

Luego abre tu navegador en:  
 [http://127.0.0.1:8000/docs#/](http://127.0.0.1:8000/docs#/)  
AhI puedeN probar la API desde la documentaciOn interactiva

---

## COmo correr pruebas

```bash
pytest
```

---

## También puede usar Docker

### 1. Construir la imagen

```bash
docker build -t cat-api .
```

### 2. Ejecutar el contenedor

```bash
docker run -d -p 8000:8000 --name cat_container cat-api
```

---

## Estructura general

- `app/` → contiene controladores, modelos, servicios y conexión a DB.
- `tests/` → pruebas automáticas.
- `.env.example` → archivo base para configuración.

---

## Nota final

Este proyecto fue desarrollado como parte de una prueba técnica. Puede mejorarse, pero cumple con los requerimientos principales: API REST, conexión externa, usuarios, autenticación y uso de Docker 
