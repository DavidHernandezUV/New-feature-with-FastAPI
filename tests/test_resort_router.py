from fastapi import FastAPI
from fastapi.testclient import TestClient
from router.resort import resort_router

app = FastAPI()

app.include_router(resort_router)

client = TestClient(app)


def test_create_first_resort():
    new_resort = {
        "name": "Nuevo Resort 1",
        "location": "New Location 1",
        "value": 5000000,
        "annual_return_investment": 10.14,
        "fractionated_percentage": 30,
        "image_url": "https://photos.zillowstatic.com/fp/f51cdee3f2f9c3883eb683a1be420a62-cc_ft_960.jpg"
}
    response = client.post("/resort/", json=new_resort)
    assert response.status_code == 200

def test_create_second_resort():
    new_resort = {
        "name": "Nuevo Resort 2",
        "location": "New Location 2",
        "value": 2000000,
        "annual_return_investment": 5.6,
        "fractionated_percentage": 50,
        "image_url": "https://photos.zillowstatic.com/fp/f51cdee3f2f9c3883eb683a1be420a62-cc_ft_960.jpg"
}
    response = client.post("/resort/", json=new_resort)
    assert response.status_code == 200
    
def test_create_third_resort():
    new_resort = {
        "name": "Casa unifamiliar",
        "location": "Cleveland – 114th St",
        "value": 5000000,
        "annual_return_investment": 10.14,
        "fractionated_percentage": 30,
        "image_url": "https://photos.zillowstatic.com/fp/f51cdee3f2f9c3883eb683a1be420a62-cc_ft_960.jpg"
    }
    response = client.post("/resort/", json=new_resort)
    assert response.status_code == 200

def test_get_resorts():
    response = client.get("/resort/")
    assert response.status_code == 200

def test_get_resort_by_id():
    response = client.get("/resort/3")
    assert response.status_code == 200

def test_delete_resort_by_id():
    response = client.delete("/resort/2")
    assert response.status_code == 200
    assert response.json()["message"] == "Resort has been deleted from the database." 

def test_update_resort_by_id():
    updated_resort = {
        "name": "Resort Actualizado",
        "location": "Ubicación Actualizada",
        "value": 4000000,
        "annual_return_investment": 9.0,
        "fractionated_percentage": 40,
        "image_url": "https://ejemplo.com/imagen-resort-actualizado.jpg"
    }
    response = client.patch("/resort/3", json=updated_resort)
    assert response.status_code == 200

def test_update_fractional_percent():
    response = client.patch("/resort/update_fractional_percent/1?percent=35.5")
    assert response.status_code == 200

def test_update_fractions_sold():
    response = client.patch("/resort/update_fractions_sold/1?fractions=10")
    assert response.status_code == 200