from fastapi import FastAPI
import uvicorn
from app.settings.settings import settings

# Routes
from app.routes.files_router import router as file_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.PROJECT_VERSION
)

# Hello World Check
@app.get(
    "/",
    description="EndPoint de verificación en la raiz para ver si el servidor esta funcionando",
    tags=["Hello World Check"]
)
async def hello_world_check():
    return {
        "titulo":app.title,
        "version":app.version
    }


# Routes

app.include_router(
    file_router,
    prefix="/file",
    tags=["Files"]
)

if __name__ == "__main__":
    uvicorn.run(
        "entrypoint:app",
        host="localhost",
        port=5000,
        reload=True
    )