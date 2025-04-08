import shutil

from fastapi import UploadFile

def upload_file(input_file:UploadFile, file_location: str):
    try:
        with open(file_location, "wb") as buffer:
            shutil.copyfileobj(input_file.file, buffer)
    finally:
        input_file.file.close()