from fastapi import APIRouter, UploadFile,File
from fastapi.responses import JSONResponse

router = APIRouter()

@router.get("/")
async def hello_world_file():
    return{
        "router":"file router"
    }

@router.post(
    "/upload",
    description="EndPoint to Upload the plain text file"
)
async def upload_file(
    file:UploadFile= File(...)
):
    
    content = await file.read()
    print(content)
    return JSONResponse(
        status_code=200,
        content={
            "msg":"File Uploaded",
            "error":None,
            "file":f"{content}"
        }
    )