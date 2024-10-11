from fastapi import APIRouter, HTTPException

from models import CommentsDB, GodsDB, HistoryDB, MytologyDB, UserDB
from schemas import CommentCreate, CommentRead, CommentReadList, HistoryRead, HistoryReadList

router = APIRouter(prefix='/comments', tags=['COMMENTS'])


@router.post('/', response_model=CommentRead)
async def create_comment(new_comment: CommentCreate):

    user = UserDB.get_or_none(UserDB.id == new_comment.id_user)
    god = GodsDB.get_or_none(GodsDB.id == new_comment.god_id)
    mytolog = MytologyDB.get_or_none(MytologyDB.id == new_comment.mytology_id)
    history = HistoryDB.get_or_none(HistoryDB.id == new_comment.history_id)

    comment = CommentsDB.create(
        comment=new_comment.comment,
        date=new_comment.date,
        last_update=new_comment.last_update,
        likes=new_comment.likes,
        status=new_comment.status,
        user=user,
        god=god,
        mytology=mytolog,
        history=history,
    )
    return comment


@router.put('/{comment_id}', response_model=CommentRead)
async def update_comment(comment_id: int, new_comment: CommentCreate):

    comment = CommentsDB.get_or_none(CommentsDB.id == comment_id)

    if comment is None:
        raise HTTPException(status_code=404, detail='Comment not found')

    for field, value in new_comment.dict(exclude_unset=True).items():
        setattr(comment, field, value)

    comment.save()

    return comment


@router.get('/', response_model=CommentReadList)
def list_comments():

    comments = CommentsDB.select()

    return {'comments': comments}


@router.get('/{comment_id}', response_model=CommentRead)
def read_comment(comment_id: int):

    comment = CommentsDB.get_or_none(CommentsDB.id == comment_id)

    if not comment:
        raise HTTPException(status_code=404, detail='Comment not found')

    return comment

@router.delete('/{comment_id}', response_model=CommentRead)
def delete_comment(comment_id: int):
    comment = CommentsDB.get_or_none(CommentsDB.id == comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail='Comment not found')
    comment.delete_instance()
    return comment

@router.get('/mitology/{mytology_id}', response_model=CommentReadList)
def read_comment_by_mytology(mytology_id: int):
    mitology = MytologyDB.get_or_none(MytologyDB.id == mytology_id)
    if not mitology:
        raise HTTPException(status_code=404, detail='Mytology not found')

    comments = CommentsDB.select().where(CommentsDB.mytology == mytology_id)

    return {'comments': comments}

@router.get('/history/{history_id}', response_model=CommentReadList)
def read_coment_by_history(history_id: int):
    history = HistoryDB.get_or_none(HistoryDB.id == history_id)

    if not history:
        raise HTTPException(status_code=404, detail='History not found')

    comment = CommentsDB.select().where(CommentsDB.history == history)

    return  {'comment': comment}

@router.get('/gods/{god_id}', response_model=CommentReadList)
def read_comment_by_god(god_id: int):
    god = GodsDB.get_or_none(GodsDB.id == god_id)
    if not god:
        raise HTTPException(status_code=404, detail='God not found')

    comment = CommentsDB.select().where(CommentsDB.god == god)

    return {'comment': comment}









