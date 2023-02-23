"""class Review"""
from base_model import BaseModel


class Review(BaseModel):
    """Review attributes"""
    place_id : str = ""
    user_id : str = ""
    test : str = ""
