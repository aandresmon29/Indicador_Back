from db.user_db import UserInDB, get_user
from db.indicador_db import IndicadorInDB, get_indicador
from models.user_models import UserIn, UserOut
from models.indicador_models import IndicadorIn,IndicadorOut
from fastapi import FastAPI
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routers.indicador_router import router as router_indicador
from routers.user_router import router as router_user

api = FastAPI()

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080","https://indicadorb.herokuapp.com",
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

api.include_router(router_user)
api.include_router(router_indicador)