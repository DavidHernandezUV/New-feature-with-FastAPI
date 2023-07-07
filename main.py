from fastapi import FastAPI
from router.resort import resort_router
from config.database import engine,Base
description = """
Macondo API helps you do awesome stuff. 🚀

## By

José David Barona Hernández.

## Resorts

You will be able to:

* **Create resorts** _Done_ 🚀.
* **Read resorts** _Done_ 🚀.
* **Update resorts** _Done_ 🚀.
* **Update fractional percent resort** _Done_ 🚀.
* **Update fractions sold** _Done_🚀.
* **Delete resorts** _Done_ 🚀.
"""

app = FastAPI(
    title="New feature Macondo App",
    description=description,
    summary="MVF",
    version="0.0.1",
)


Base.metadata.create_all(bind=engine)

app.include_router(resort_router)