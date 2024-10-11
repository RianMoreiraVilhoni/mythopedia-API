from peewee import (
    AutoField,
    CharField,
    DateField,
    DateTimeField,
    ForeignKeyField,
    IntegerField,
    Model,
)

from config.database import database


class UserDB(Model):
    id = AutoField()
    name = CharField()
    email = CharField()
    password = CharField()
    type = IntegerField()

    class Meta:
        database = database
        table_name = 'user'


class MytologyDB(Model):
    id = AutoField()
    name = CharField()
    sub_description = CharField()
    description = CharField()
    origin = CharField()
    period = CharField()
    gods_qty = IntegerField()
    sacred_texts = CharField()
    main_mytology = CharField()
    main_symbol = CharField()
    mytology_banner = CharField()
    mytology_profile_img = CharField()
    creator = CharField()
    data_creation = DateField()
    last_update = DateField()

    class Meta:
        database = database
        table_name = 'mytology'


class GodsDB(Model):
    id = AutoField()
    name = CharField()
    sub_description = CharField()
    description = CharField()
    symbol = CharField()
    domain = CharField()
    kinship = CharField()
    caracteristics = CharField()
    sacred_animal = CharField()
    sacred_colour = CharField()
    data_creation = DateField()
    last_update = DateField()

    class Meta:
        database = database
        table_name = 'gods'


class HistoryDB(Model):
    id = AutoField()
    title = CharField()
    content = CharField()
    author = CharField()
    source = CharField()
    publish_time = DateTimeField()
    last_updated = DateTimeField()
    views = IntegerField()
    age_classification = IntegerField()
    god = ForeignKeyField(model=GodsDB, backref='stories')
    mythology = ForeignKeyField(MytologyDB, backref='stories')

    class Meta:
        database = database
        table_name = 'history'


class CommentsDB(Model):
    id = AutoField()
    comment = CharField()
    date = DateTimeField()
    last_update = DateTimeField()
    likes = IntegerField()
    status = IntegerField()
    user = ForeignKeyField(UserDB, backref='comments')
    god = ForeignKeyField(GodsDB, backref='comments', null=True)
    mytology = ForeignKeyField(MytologyDB, backref='comments', null=True)
    history = ForeignKeyField(HistoryDB, backref='comments', null=True)

    class Meta:
        database = database
        table_name = 'comments'
