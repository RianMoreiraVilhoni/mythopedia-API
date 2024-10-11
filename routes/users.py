from fastapi import APIRouter, HTTPException

from models import UserDB
from schemas import UserCreate, UserRead, UserReadList, UserUpdate

router = APIRouter(prefix='/users', tags=['USERS'])


@router.post('', response_model=UserRead)
def create_user(new_user: UserCreate):

    user = UserDB.create(**new_user.model_dump())

    return user


@router.get('', response_model=UserReadList)
def list_user():

    users = UserDB.select()

    return {'users': users}


@router.get('/{user_id}', response_model=UserRead)
def read_user(user_id: int):

    user = UserDB.get_or_none(UserDB.id == user_id)

    if not user:
        raise HTTPException(status_code=404, detail='User not found')
    return user


@router.put('/{user_id}', response_model=UserRead)
def update_user(user_id: int, updated_user: UserUpdate):

    user = UserDB.get_or_none(UserDB.id == user_id)

    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    user.name = updated_user.name
    user.email = updated_user.email
    user.password = updated_user.password
    user.type = updated_user.type

    user.save()

    return user


@router.delete('/{user_id}', response_model=UserRead)
def delete_user(user_id: int):

    user = UserDB.get_or_none(UserDB.id == user_id)

    if not user:
        raise HTTPException(status_code=404, detail='User not found')

    user.delete_instance()

    return user
