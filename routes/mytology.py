import os
import shutil
from typing import Annotated

from fastapi import APIRouter, File, HTTPException, UploadFile

from models import MytologyDB
from schemas import (
    MytologyCreate,
    MytologyRead,
    MytologyReadList,
    MytologyUpdate,
)

router = APIRouter(prefix='/mythologies', tags=['MYTHOLOGIES'])

UPLOAD_DIRECTORY = 'uploads'
os.makedirs(UPLOAD_DIRECTORY, exist_ok=True)


@router.post('/files/')
async def create_file(fileb: Annotated[UploadFile, File()]):

    file_location = f'{UPLOAD_DIRECTORY}/{fileb.filename}'

    with open(file_location, 'wb') as file:
        shutil.copyfileobj(fileb.file, file)

    return {'file_location': file_location}


@router.post('', response_model=MytologyRead)
def create_mytology(new_mytology: MytologyCreate):

    mytology = MytologyDB.create(**new_mytology.model_dump())

    return mytology


@router.put('/{mythology_id}', response_model=MytologyRead)
def update_mytology(mythology_id: int, updated_mytology: MytologyUpdate):

    mytology = MytologyDB.get_or_none(MytologyDB.id == mythology_id)

    if not mytology:
        raise HTTPException(status_code=404, detail='Mythology not found')

    for field, value in updated_mytology.model_dump(
        exclude_unset=True
    ).items():
        setattr(mytology, field, value)

    mytology.save()

    return mytology


@router.get('', response_model=MytologyReadList)
def list_mytology():

    mytologies = MytologyDB.select()

    return {'mytologies': mytologies}


@router.get('/{mythology_id}', response_model=MytologyRead)
def read_mytology(mythology_id: int):

    mytology = MytologyDB.get_or_none(MytologyDB.id == mythology_id)

    if not mytology:
        raise HTTPException(status_code=404, detail='Mythology not found')

    return mytology


@router.delete('/{mythology_id}', response_model=MytologyRead)
def delete_mytology(mythology_id: int):

    mytology = MytologyDB.get_or_none(MytologyDB.id == mythology_id)

    if not mytology:
        raise HTTPException(status_code=404, detail='Mythology not found')
    mytology.delete_instance()
    return mytology
