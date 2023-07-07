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
    """
    ## ARGS
        - id: Int
    """
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
    """
    ## ARGS
        - id: Int
    """
    result = ResortService(Session()).delete_resort_by_id(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Resort does NOT exist in the database."})
    
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Resort has been deleted from the database."}) 
    
    
@resort_router.patch('/{id}',status_code=status.HTTP_200_OK, tags=["Resorts"],response_model=Resort,summary="This endpoint update a resort by id")
def update_resort_by_id(id: int, resort_updated: Resort):
    """
    ## ARGS
        - id: Int
        - resort_updated: Resort
    """
    result = ResortService(Session()).get_resort_by_id(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Resort does NOT exist in the database."})
    resort_data = resort_updated.dict(exclude_unset=True)
    ResortService(Session()).update_resort(resort_data,result)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Resort was successfully updated."}) 


@resort_router.patch('/update_fractional_percent/{id}',status_code=status.HTTP_200_OK, tags=["Resorts"],response_model=Resort,summary="This endpoint update fractional percent of resort by id")
def update_fractional_percent(id: int, percent: float):
    """
    ## ARGS
        - id: Int
        - percent: Float
    ## Description
        - This endpoint is used to update the fractional percent for a specific resort identified by its ID. It also automatically updates the available fractions.
    """
    result = ResortService(Session()).get_resort_by_id(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Resort does NOT exist in the database."})
    ResortService(Session()).update_fractional_percent_resort(percent,result)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Resort was successfully updated."})


@resort_router.patch('/update_fractions_sold/{id}',status_code=status.HTTP_200_OK, tags=["Resorts"],response_model=Resort,summary="This endpoint update fractions sold of resort by id")
def update_fractions_sold(id:int,fractions:int):
    """
    ## ARGS
        - id: Int
        - fractions: Float
        
    ## Description
        - This endpoint is used to update the number of fractions sold for a specific resort identified by its ID. It also automatically updates the available fractions.
    """
    result = ResortService(Session()).get_resort_by_id(id)
    if not result:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "Resort does NOT exist in the database."})
    if result.fractions_available < fractions:
        return JSONResponse(status_code=status.HTTP_404_NOT_FOUND, content={"message": "The requested number of fractions exceeds the available fractions for the resort."})
    ResortService(Session()).update_fractions_sold_resort(fractions,result)
    return JSONResponse(status_code=status.HTTP_200_OK, content={"message": "Resort fractions were successfully updated."})