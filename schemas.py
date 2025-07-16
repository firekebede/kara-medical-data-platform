from pydantic import BaseModel
from typing import List

class TopProduct(BaseModel):
    product: str
    mention_count: int

class ChannelActivity(BaseModel):
    date: str
    message_count: int

class MessageResult(BaseModel):
    id: int
    channel: str
    message: str
    date: str
