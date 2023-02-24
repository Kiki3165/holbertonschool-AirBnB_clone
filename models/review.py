"""class Review"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Review attributes"""
    place_id : str = ""
    user_id : str = ""
    text : str = ""
