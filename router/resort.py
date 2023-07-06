from fastapi import APIRouter, status, Path
from config.database import Session
from schema.resort import Resort
from services.resort import ResortService
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import List

resort_router = APIRouter(prefix='/resort', tags=['Resorts'])

@resort_router.get('/',status_code=status.HTTP_200_OK, tags=["Resorts"],response_model=List[Resort],summary="This endpoint returns all resorts")
def get_resorts():
    """
    ## RESPONSE
        - resorts: List(Resort)
    """
    result = ResortService(Session()).get_resorts()
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))


@resort_router.get('/{id}',status_code=status.HTTP_200_OK, tags=["Resorts"],response_model=Resort,summary="This endpoint return a resort by id")
def get_resort_by_id(id: int = Path(ge=1)):
    
    result = ResortService(Session()).get_resort_by_id(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Resort does NOT exist in the database."})
    
    return JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))

@resort_router.post('/',status_code=status.HTTP_201_CREATED,response_model=Resort,tags=['Resorts'],summary="This endpoint create a resort")
def create_resort(resort: Resort):
    """
    ## ARGS
        - resort: Resort
    ## RESPONSE
        - resort: Resort
    """
    result = ResortService(Session()).create_resort(resort)

    return  JSONResponse(status_code=status.HTTP_200_OK, content=jsonable_encoder(result))


@resort_router.delete('/{id}',status_code=status.HTTP_200_OK, tags=["Resorts"],response_model=Resort,summary="This endpoint delete a resort by id")
def delete_resort_by_id(id: int = Path(ge=1)):
    result = ResortService(Session()).delete_resort_by_id(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Resort does NOT exist in the database."})
    
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Resort has been deleted from the database."}) 
    
    
@resort_router.patch('/{id}',status_code=status.HTTP_200_OK, tags=["Resorts"],response_model=Resort,summary="This endpoint update a resort by id")
def update_resort_by_id(id: int, resort_updated: Resort):
    result = ResortService(Session()).get_resort_by_id(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Resort does NOT exist in the database."})
    resort_data = resort_updated.dict(exclude_unset=True)
    ResortService(Session()).update_resort(resort_data,result)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Resort was successfully updated."}) 


@resort_router.patch('/update_fractional_percent/{id}',status_code=status.HTTP_200_OK, tags=["Resorts"],response_model=Resort,summary="This endpoint update fractional percent of resort by id")
def update_fractional_percent(id: int, percent: float):
    result = ResortService(Session()).get_resort_by_id(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Resort does NOT exist in the database."})
    ResortService(Session()).update_fractional_percent_resort(percent,result)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Resort was successfully updated."}) 
    
# @resort_router.put("/")
# def update_resort(updated_resort: Resort):
#     resort.name = updated_resort.name
#     resort.location = updated_resort.location
#     resort.annual_returns = updated_resort.annual_returns
#     resort.fractionated_percentage = updated_resort.fractionated_percentage
#     resort.image_url = updated_resort.image_url
    
#     # Calculate the number of fractions available based on the fractionated percentage
#     total_resort_cost = 5000000  # Total cost of the resort
#     fraction_cost = 50  # Cost of each fraction
#     fractionated_percentage = resort.fractionated_percentage
#     fractions_available = int((total_resort_cost * (fractionated_percentage / 100)) / fraction_cost)
#     resort.fractions_available = fractions_available
    
#     return {"message": "Resort updated successfully."}

# @resort_router.post('/',status_code=status.HTTP_201_CREATED, tags=['Resorts'], response_model=Resort,summary="This endpoint create a resort")
# def create_resort(resort:Resort):
#     db = Session()
#     new_resort = Resort(**resort.dict())
#     return new_resort.dict()