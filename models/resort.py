
from sqlalchemy import Column,Integer, String, Float
from config.database import Base


class Resort(Base):
    __tablename__= "resorts"
    
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    location = Column(String)
    value = Column(Integer)
    annual_return_investment = Column(Float)
    fractionated_percentage = Column(Float)
    fractions_sold = Column(Integer,default=0)
    fractions_available = Column(Integer)
    total_fractions = Column(Integer)
    image_url = Column(String)