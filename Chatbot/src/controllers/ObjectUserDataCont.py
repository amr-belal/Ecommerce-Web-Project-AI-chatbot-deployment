from pydantic import BaseModel
from typing import List, Optional

class ObjectUserData(BaseModel):
    name: str
    email: Optional[str] = None 
    message: str
    
class Location(BaseModel):
    lat: float
    lng: float
    city: str
    country: str
    address: str
class ChatResponse(BaseModel):
    reply :str 
    location :List 
    keywords :list[str] = []
    weather :List
    recommend_products: Optional[List[str]] = []
