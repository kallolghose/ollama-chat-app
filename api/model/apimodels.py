from pydantic import BaseModel

class UploadSuccessResponse(BaseModel):
    status: str
    message: str

class ChatResponse(BaseModel):
    llmResponse: str