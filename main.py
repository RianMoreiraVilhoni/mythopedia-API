from logging import shutdown
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from config.database import shutdown_db, startup_db
from routes.comments import router as comments_router
from routes.gods import router as gods_router
from routes.history import router as history_router
from routes.mytology import router as mytology_router
from routes.users import router as users_router

app = FastAPI(title='API DE MITOLOGIAS')

app.add_event_handler('startup', func=startup_db)
app.add_event_handler('shutdown', func=shutdown_db)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*'],
)

app.mount("/uploads", StaticFiles(directory="uploads"), name="uploads")
@app.get('/')
def read_root():
    return {'message': 'the bluethoot device is conected succesfully'}

@app.get("/images/{image_name}")
async def serve_image(image_name: str):
    image_path = f"uploads/{image_name}"
    if os.path.exists(image_path):
        return FileResponse(image_path)
    return {"error": "Image not found"}


app.include_router(users_router)
app.include_router(gods_router)
app.include_router(mytology_router)
app.include_router(history_router)
app.include_router(comments_router)
