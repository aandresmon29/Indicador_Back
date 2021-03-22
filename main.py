from db.user_db import UserInDB, get_user
from db.indicador_db import IndicadorInDB, get_indicador
from models.user_models import UserIn, UserOut
from models.indicador_models import IndicadorIn,IndicadorOut
from fastapi import FastAPI
from fastapi import HTTPException

api = FastAPI()

@api.get("/user/info/{username}")
async def get_name(username: str):
    user_in_db = get_user(username)
    if user_in_db == None:
        raise HTTPException(status_code=404, detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())
    return user_out

@api.get("/Indicadores/{indicador}")
async def get_indicor(indicador: str):
    Indicador_in_db = get_indicador(indicador)
    if Indicador_in_db == None:
        raise HTTPException(status_code=404, detail="El indicador no existe")
    indicador_out = IndicadorOut(**Indicador_in_db.dict())
    return indicador_out