import os
import shutil
from typing import Annotated

from fastapi import APIRouter, File, HTTPException, UploadFile

from models import GodsDB, HistoryDB, MytologyDB
from schemas import HistoryCreate, HistoryRead, HistoryReadList, HistoryUpdate

router = APIRouter(prefix='/history', tags=['STORIES'])

UPLOAD_DIRECTORY = 'uploads'
if not os.path.exists(UPLOAD_DIRECTORY):
    os.makedirs(UPLOAD_DIRECTORY)


@router.post('/files/', response_model=HistoryRead)
async def create_file(fileb: Annotated[UploadFile, File()]):
    file_location = f'{UPLOAD_DIRECTORY}/{fileb.filename}'
    with open(file_location, 'wb') as file:
        shutil.copyfileobj(fileb.file, file)
    return {'file_location': file_location}


@router.post('', response_model=HistoryRead)
def create_history(new_history: HistoryCreate):
    god = GodsDB.get_or_none(GodsDB.id == new_history.god_id)

    mythology = MytologyDB.get_or_none(
        MytologyDB.id == new_history.mythology_id
    )

    if not god:
        raise HTTPException(status_code=404, detail='God not found')

    if not mythology:
        raise HTTPException(status_code=404, detail='Mythology not found')

    history = HistoryDB.create(
        title=new_history.title,
        content=new_history.content,
        author=new_history.author,
        source=new_history.source,
        publish_time=new_history.publish_time,
        last_updated=new_history.last_updated,
        views=new_history.views,
        age_classification=new_history.age_classification,
        mythology=mythology,
        god=god,
    )

    return history


@router.put('/{story_id}', response_model=HistoryRead)
def update_history(story_id: int, updated_history: HistoryUpdate):
    history = HistoryDB.get_or_none(HistoryDB.id == story_id)
    if not history:
        raise HTTPException(status_code=404, detail='History not found')

    for field, value in updated_history.model_dump(exclude_unset=True).items():
        setattr(history, field, value)

    history.save()

    return history


@router.get('/stories', response_model=HistoryReadList)
def list_stories():
    stories = HistoryDB.select()
    return {'stories': stories}


@router.get('/{story_id}', response_model=HistoryRead)
def read_history(story_id: int):
    history = HistoryDB.get_or_none(HistoryDB.id == story_id)

    if not history:
        raise HTTPException(status_code=404, detail='History not found')

    return history


@router.delete('/{story_id}', response_model=HistoryRead)
def delete_history(story_id: int):
    history = HistoryDB.get_or_none(HistoryDB.id == story_id)

    if not history:
        raise HTTPException(status_code=404, detail='History not found')

    history.delete_instance()

    return history


@router.get('/gods/{god_id}', response_model=HistoryReadList)
def read_history_by_god(god_id: int):
    god = GodsDB.get_or_none(GodsDB.id == god_id)

    if not god:
        raise HTTPException(status_code=404, detail='God not found')

    stories = HistoryDB.select().where(HistoryDB.god == god)

    return {'stories': stories}
