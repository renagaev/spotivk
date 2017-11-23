from peewee import *

db = SqliteDatabase('db.db')


class BaseModel(Model):
    class Meta:
        database = db


class User(BaseModel):
    vk_id = IntegerField()
    state = CharField()
    spotify_token = CharField()
    spotify_username = CharField()


class Playlist(BaseModel):
    owner = ForeignKeyField(User, related_name='playlists')
    name = CharField()
    uri = CharField()
    spotify_id = CharField()
    public = BooleanField()

