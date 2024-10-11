from datetime import datetime

from pydantic import BaseModel


class UserCreate(BaseModel):
    name: str
    email: str
    password: str
    type: int


class UserRead(BaseModel):
    id: int
    name: str
    email: str
    type: int

    class Config:
        from_attributes = True


class UserUpdate(BaseModel):
    name: str | None
    email: str | None
    password: str | None
    type: int | None


class UserReadList(BaseModel):
    users: list[UserRead]


class CommentCreate(BaseModel):
    id_user: int
    comment: str
    date: datetime
    last_update: datetime
    likes: int
    status: int
    god_id: int | None = None
    mytology_id: int | None = None
    history_id: int | None = None


class GodsCreate(BaseModel):
    name: str
    sub_description: str
    description: str
    symbol: str
    domain: str
    kinship: str
    caracteristics: str
    sacred_animal: str
    sacred_colour: str
    data_creation: datetime
    last_update: datetime

    class Config:
        from_attributes = True


class GodsRead(BaseModel):
    id: int
    name: str
    sub_description: str
    description: str
    symbol: str
    domain: str
    kinship: str
    caracteristics: str
    sacred_animal: str
    sacred_colour: str
    data_creation: datetime
    last_update: datetime

    class Config:
        from_attributes = True


class GodsReadShort(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class GodsUpdate(BaseModel):
    name: str | None
    sub_description: str | None
    description: str | None
    symbol: str | None
    domain: str | None
    kinship: str | None
    caracteristics: str | None
    sacred_animal: str | None
    sacred_colour: str | None
    data_creation: datetime | None
    last_update: datetime | None

    class Config:
        from_attributes = True


class GodsReadList(BaseModel):
    gods: list[GodsRead]

    class Config:
        from_attributes = True


# Schema para Histórias
class HistoryCreate(BaseModel):
    title: str
    content: str
    author: str
    source: str
    publish_time: datetime
    last_updated: datetime
    views: int
    age_classification: int
    mythology_id: int
    god_id: int


class MytologyReadShort(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class HistoryRead(BaseModel):
    id: int
    title: str
    content: str
    author: str
    source: str
    publish_time: datetime
    last_updated: datetime
    views: int
    age_classification: int
    god: GodsReadShort
    mythology: MytologyReadShort

    class Config:
        from_attributes = True


class HistoryReadShort(BaseModel):
    id: int
    title: str

    class Config:
        from_attributes = True


class HistoryUpdate(BaseModel):
    mythology_id: int | None
    title: str | None
    content: str | None
    author: str | None
    source: str | None
    publish_time: datetime | None
    last_updated: datetime | None
    views: int | None
    age_classification: int | None
    god: GodsRead | None


class HistoryReadList(BaseModel):
    stories: list[HistoryRead]


class MytologyCreate(BaseModel):
    name: str
    sub_description: str
    description: str
    origin: str
    period: str
    gods_qty: int
    sacred_texts: str
    main_mytology: str
    creator: str
    data_creation: datetime
    last_update: datetime
    main_symbol: str
    mytology_banner: str
    mytology_profile_img: str


class MytologyRead(BaseModel):
    id: int
    name: str
    sub_description: str
    description: str
    origin: str
    period: str
    gods_qty: int
    sacred_texts: str
    main_mytology: str
    creator: str
    data_creation: datetime
    last_update: datetime
    main_symbol: str
    mytology_banner: str
    mytology_profile_img: str

    class Config:
        from_attributes = True


class MytologyUpdate(BaseModel):
    name: str | None
    sub_description: str | None
    description: str | None
    origin: str | None
    period: str | None
    gods_qty: int | None
    sacred_texts: str | None
    main_mytology: str | None
    creator: str | None
    data_creation: datetime | None
    last_update: datetime | None
    main_symbol: str | None
    mytology_banner: str | None
    mytology_profile_img: str | None


class MytologyReadList(BaseModel):
    mytologies: list[MytologyRead]


class MytologyReadListWithHistory(BaseModel):
    name: str
    sub_description: str
    description: str
    origin: str
    period: str
    gods_qty: int
    sacred_texts: str
    main_mytology: str
    creator: str
    data_creation: datetime
    last_update: datetime
    main_symbol: str
    mytology_banner: str
    mytology_profile_img: str
    stories: list[HistoryRead]


class CommentRead(BaseModel):
    id: int
    comment: str
    date: datetime
    last_update: datetime
    likes: int
    status: int
    user: UserRead
    god: GodsReadShort | None
    mytology: MytologyReadShort | None
    history: HistoryReadShort | None

    class Config:
        from_attributes = True


class CommentUpdate(BaseModel):
    id_user: int | None
    comment: str | None
    date: datetime | None
    last_update: datetime | None
    likes: int | None
    status: int | None
    god_id: int | None
    mytology_id: int | None
    history_id: int | None


class CommentReadList(BaseModel):
    comments: list[CommentRead]

    class Config:
        from_attributes = True
