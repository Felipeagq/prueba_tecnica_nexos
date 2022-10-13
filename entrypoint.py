from fastapi import FastAPI
import uvicorn

app = FastAPI(
    title="Prueba Tecnica Nexos",
    version="v0.0.1"
)

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


if __name__ == "__main__":
    uvicorn.run(
        "entrypoint:app",
        host="localhost",
        port=5000,
        reload=True
    )