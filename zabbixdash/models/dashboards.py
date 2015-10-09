from peewee import *

db = SqliteDatabase('dashboards.db')

# Environment Definitions
class User(Model):
    id = PrimaryKeyField()
    name = CharField()

    class Meta:
        database = db


class Dashboard(Model):
    id = PrimaryKeyField()
    name = CharField()
    created = DateTimeField()
    user = ForeignKeyField(User, related_name='dashboards')

    class Meta:
        database = db


class Server(Model):
    id = PrimaryKeyField()
    host = CharField()
    token = CharField()

    class Meta:
        database = db


class Item(Model):
    id = PrimaryKeyField()
    server = ForeignKeyField(Server, related_name='items')
    dashboard = ForeignKeyField(Dashboard, related_name='items')
    itemid = IntegerField()

    class Meta:
        database = db


def create_tables():
    tables = [Dashboard, User, Server, Item]
    for table in tables:
        try:
            table.create_table()
        except OperationalError as e:
            if 'already exists' in str(e):
                pass
            else:
                exit('Fatal Error')
    return tables

if __name__ == '__main__':
    create_tables()
