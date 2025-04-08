from fastapi import FastAPI, File, UploadFile, HTTPException

from api.custom_chat import ChatApplication
from api.milvus_db_operations import MilvusDB
from api.model.apimodels import UploadSuccessResponse, ChatResponse
from api.model.utilities import upload_file

app = FastAPI()
chat = ChatApplication()
milvusDB = MilvusDB("langchain_demo")

@app.get("/chat")
async def root(query: str = ""):
    agent_response = chat.ask(query)
    return ChatResponse(llmResponse=agent_response)

@app.post("/upload", response_model=UploadSuccessResponse)
async def upload_info(file: UploadFile = File(...)):
    """
    Upload File
    :param file:
    :return:
    """
    if file.content_type != 'application/pdf':
        raise HTTPException(status_code=400, detail="Only pdf files are allowed")
    upload_file(file, f"uploaded/{file.filename}")
    chat.ingest(f"uploaded/{file.filename}")
    return UploadSuccessResponse(status="success", message="File was uploaded to the model.")

