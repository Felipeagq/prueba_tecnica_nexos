from fastapi import APIRouter, UploadFile,File
from fastapi.responses import JSONResponse

import os
from datetime import datetime

from app.settings.settings import settings
from app.db.postgres.pg_core import engine
from app.services import update_sql
from app.services.aws_service import cliente_aws,upload_to_s3
from app.models.inventory_model import InventoryModel

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
        
        # Create aws_client
        aws_client = cliente_aws(
            settings.ACCESS_KEY_ID,
            settings.SECRET_ACCESS_KEY,
            "s3"
        )
        print(aws_client)
        print()
        
        name = f"{datetime.now()}"
        name = name.replace(" ","").replace(":","")
        
        # Upload file to s3
        response = upload_to_s3(
            aws_client=aws_client,
            file_data=content,
            bucket_name="testing-files-felipe",
            file_name=f"nexos/inventario/{name}.csv"
        )
        print(response)
        
        # Save File
        with open(file_path,"wb") as file:
            file.write(content)
            file.close()

        # Process File
        df = update_sql.load_csv(file_path)
        state = update_sql.load_to_sql(
            df=df,
            table_name= InventoryModel.__tablename__,
            motor=engine
        )
        
        return JSONResponse(
            status_code=200,
            content={
                "msg":"File Uploaded",
                "error":None,
                "data":f"{state}"
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



@router.get("/file")
def list_files():
    try:
        aws_client = cliente_aws(
            settings.ACCESS_KEY_ID,
            settings.SECRET_ACCESS_KEY,
            "s3"
        )
        response_list_files = aws_client.list_objects(
            Bucket="testing-files-felipe",
            Prefix="nexos/inventario/"
        )
        print(response_list_files)
        # list_list_files = [i.get("Key",None).split("/")[2] for i in response_list_files.get("Contents",None)]
        list_list_files = [i.get("Key",None) for i in response_list_files.get("Contents",None)]
        return JSONResponse(
            content={
                # "response":response_list_files,
                "list":list_list_files
            }
        )
    except Exception as e:
        return JSONResponse(
            content={
                "msg":"Cant list objects",
                "error":True,
                "data":f"{e} - {e.__class__}"
            }
        )


# @router.get("/file/download/{file}")
# def download_file(
#     file
# ):
#     try:
#         aws_client = cliente_aws(
#             settings.ACCESS_KEY_ID,
#             settings.SECRET_ACCESS_KEY,
#             "s3"
#         )
#         print(file)
#         print(f"------nexos/inventario/{file}")
#         aws_client.download_file(
#             Bucket= "testing-files-felipe",
#             Key=f"nexos/inventario/{file}",
#             Filename= f"{file}"
#         )
#         return {
#             "downloaded":"i dont know"
#         }
#     except Exception as e:
#         return {
#             "error":f"{e}"
#         }