"""class User"""
from base_model import BaseModel


class User(BaseModel):
    """User attributes"""
    email: str = ""
    password: str = ""
    first_name: str = ""
    last_name: str =""
