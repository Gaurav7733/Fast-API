from fastapi import FastAPI
from Routs.routs import router

app = FastAPI()

app.include_router(router)