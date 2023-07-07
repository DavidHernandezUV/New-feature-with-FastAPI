from models.resort import Resort as ResortModel
from schema.resort import Resort


class ResortService():
    
    def __init__(self,db) -> None:
        self.db = db
        self.fixed_cost_per_fraction = 50 #50 dlls
        
    def create_resort(self,resort:Resort):
        new_resort = ResortModel(**resort.dict())
        fractions  = int((new_resort.value * (new_resort.fractionated_percentage / 100)) / self.fixed_cost_per_fraction)
        new_resort.total_fractions = fractions
        new_resort.fractions_available = fractions
        self.db.add(new_resort)
        self.db.commit()
        self.db.refresh(new_resort)
        self.db.close()
        return new_resort
    
    def get_resorts(self):
        result = self.db.query(ResortModel).all()
        self.db.close()
        return result
    
    def get_resort_by_id(self,id:int):
        result = self.db.query(ResortModel).filter(ResortModel.id == id).first()
        self.db.close()
        return result
    
    def delete_resort_by_id(self,id:int):
        result = self.db.query(ResortModel).filter(ResortModel.id == id).delete()
        self.db.commit()
        self.db.close()
        return result
    
    def update_resort(self, resort: Resort, result: Resort):
        
        for key, value in resort.items():
            setattr(result,key,value)
        result.total_fractions  = int((result.value * (result.fractionated_percentage / 100)) / self.fixed_cost_per_fraction)
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)
        self.db.close()
        return
    
    def update_fractional_percent_resort(self,percent:float,result:Resort):
        
        available = int((result.value * (percent / 100)) / self.fixed_cost_per_fraction)
        
        #pre-update
        result.fractionated_percentage = percent
        result.total_fractions = available
        result.fractions_available = result.total_fractions-result.fractions_sold
        
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)
        self.db.close()
        return
    
    def update_fractions_sold_resort(self,fractions:int,result:Resort):
        #pre-update
        result.fractions_sold += fractions
        result.fractions_available = result.total_fractions-result.fractions_sold
        
        self.db.add(result)
        self.db.commit()
        self.db.refresh(result)
        self.db.close()
        return