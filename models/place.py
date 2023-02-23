"""class Place"""
from models.base_model import BaseModel


class Place(BaseModel):
    """Place attributes"""
    city_id: str = ""
    user_id: str = ""
    name: str = ""
    description: str =""
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = float(0.0)
    longitude = float(0.0)
    amenity_ids = []
