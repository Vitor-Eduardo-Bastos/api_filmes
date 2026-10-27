from fastapi import FastAPI

import database
from filmes_routers import router


app = FastAPI()

app.include_router(router)
