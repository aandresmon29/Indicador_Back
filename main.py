from fastapi import FastAPI, applications
from fastapi import HTTPException
from fastapi.middleware.cors import CORSMiddleware
from routers.indicador_router import router as router_indicador
from routers.user_router import router as router_user
from routers.gerencia_router import router as router_gerencia

api = FastAPI()

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080","https://indivp.herokuapp.com",
]

api.add_middleware(
    CORSMiddleware, allow_origins=origins,
    allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

api.include_router(router_user)
api.include_router(router_indicador)
api.include_router(router_gerencia)