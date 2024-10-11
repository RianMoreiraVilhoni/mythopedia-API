import os
import shutil
from typing import Annotated

from fastapi import APIRouter, File, HTTPException, UploadFile

from models import GodsDB
from schemas import GodsCreate, GodsRead, GodsReadList, GodsUpdate

router = APIRouter(prefix='/gods', tags=['GODS'])

UPLOAD_DIRECTORY = 'uploads'

os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)


@router.post('/files/')
async def create_file(fileb: Annotated[UploadFile, File()]):

    file_location = os.path.join(UPLOAD_DIRECTORY, fileb.filename)

    with open(file_location, 'wb') as file:
        shutil.copyfileobj(fileb.file, file)

    return {'file_location': file_location}


@router.post('', response_model=GodsRead)
def create_gods(new_god: GodsCreate):

    god = GodsDB.create(**new_god.model_dump())

    return god


@router.put('/{gods_id}', response_model=GodsRead)
def update_gods(gods_id: int, updated_god: GodsUpdate):

    god = GodsDB.get_or_none(GodsDB.id == gods_id)

    if not god:
        raise HTTPException(status_code=404, detail='God not found')

    for field, value in updated_god.dict().items():
        setattr(god, field, value)

    god.save()

    return god


@router.get('', response_model=GodsReadList)
def list_gods():

    gods = GodsDB.select()

    return {'gods': gods}


@router.get('/{god_id}', response_model=GodsRead)
def read_gods(god_id: int):

    god = GodsDB.get_or_none(GodsDB.id == god_id)

    if not god:
        raise HTTPException(status_code=404, detail='God not found')

    return god


@router.delete('/{god_id}', response_model=GodsRead)
def delete_god(god_id: int):

    god = GodsDB.get_or_none(GodsDB.id == god_id)

    if not god:
        raise HTTPException(status_code=404, detail='God not found')

    god.delete_instance()

    return god
