from pydantic import BaseModel, Field
from typing import Optional

class Resort(BaseModel):
    id: Optional[int] = None
    name: str = Field(default="New Resort", min_length=1, max_length=50)
    location: str = Field(..., min_length=1, max_length=100)
    value: int = Field(...,ge=0)
    annual_return_investment: float = Field(..., ge=0)
    fractionated_percentage: float = Field(..., ge=0, le=100)
    image_url: str = Field(..., min_length=1)
    
    
    class Config:
        schema_extra = {
            "example":{
                "name":"Casa unifamiliar",
                "location":"Cleveland – 114th St",
                "value": 5000000,
                "annual_return_investment":10.14,
                "fractionated_percentage":30,
                "image_url":"https://photos.zillowstatic.com/fp/f51cdee3f2f9c3883eb683a1be420a62-cc_ft_960.jpg"
            }

        }