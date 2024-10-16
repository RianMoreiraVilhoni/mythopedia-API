from peewee import MySQLDatabase

database = MySQLDatabase(
    'mitologias',
    user='root',
    host='127.0.0.1',
    port=3306
)


def startup_db():
    database.connect()

    from models import CommentsDB, GodsDB, HistoryDB, MytologyDB, UserDB

    database.create_tables([UserDB, MytologyDB, HistoryDB, GodsDB, CommentsDB])


def shutdown_db():
    database.close()
