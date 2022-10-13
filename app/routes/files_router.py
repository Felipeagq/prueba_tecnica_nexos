from fastapi import APIRouter, UploadFile,File
from fastapi.responses import JSONResponse

import os
import pandas as pd

from app.settings.settings import settings
from app.db.postgres.pg_core import engine

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
    try:
        # Read File
        file_path = os.path.join(settings.STORAGE_PATH,file.filename)
        print(file_path)
        content = await file.read()
        
        # Save File
        with open(file_path,"wb") as file:
            file.write(content)
            file.close()

        # Process File
        df = pd.read_csv(file_path)
        print(df)
        df.to_sql(
            'inventory2', 
            engine,
            index=False, # Not copying over the index,
            if_exists="append"
        )
        
        return JSONResponse(
            status_code=200,
            content={
                "msg":"File Uploaded",
                "error":None,
                "data":f"{content}"
            }
        )
    except Exception as e:
        print(e,e.__class__)
        return JSONResponse(
            content={
                "msg":"File Not Uploaded correctly",
                "error":True,
                "data":f"{e} - {e.__class__}"
            }
        )