from fastapi import FastAPI
from router.resort import resort_router
from config.database import engine,Base
app = FastAPI()


Base.metadata.create_all(bind=engine)

app.include_router(resort_router)