"""class City"""
from models.base_model import BaseModel


class City(BaseModel):
    """City attributes"""
    state_id: str = ""
    name: str = ""
