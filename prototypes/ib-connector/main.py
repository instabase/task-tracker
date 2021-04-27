from fastapi import FastAPI
from routers import zenefits, breezyhr

app = FastAPI()
app.include_router(zenefits.router)
app.include_router(breezyhr.router)