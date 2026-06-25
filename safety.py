from pydantic import BaseModel, Field

class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)
    user_id: str | None = None
    locale: str | None = "en"

class ChatResponse(BaseModel):
    reply: str
    disclaimer: str
    safety_level: str = "general"
