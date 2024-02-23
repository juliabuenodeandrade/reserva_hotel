from pydantic import BaseModel, Field
from datetime import date

class Reservation(BaseModel):
    name: str = Field(..., example="John Doe")
    hotel_name: str = Field(..., example="Hotel California")
    check_in: date = Field(..., example="2023-01-01")
    check_out: date = Field(..., example="2023-01-05")

    class Config:
        schema_extra = {
            "example": {
                "name": "John Doe",
                "hotel_name": "Hotel California",
                "check_in": "2023-01-01",
                "check_out": "2023-01-05"
            }
        }
