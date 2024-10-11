from peewee import SqliteDatabase

database = SqliteDatabase('database-v2.db')


def startup_db():
    database.connect()

    from models import CommentsDB, GodsDB, HistoryDB, MytologyDB, UserDB

    database.create_tables([UserDB, MytologyDB, HistoryDB, GodsDB, CommentsDB])


def shutdown_db():
    database.close()
