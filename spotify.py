from spotipy import oauth2
import spotipy
import asyncio
from functools import partial



class SpotifyTokenGetter(oauth2.SpotifyOAuth):
    def __init__(self, app_credentials: dict, username: str):
        scopes = ' '.join(['playlist-read-private',
                           'playlist-modify-private',
                           'user-library-read',
                           'user-library-modify'
                           ])
        client_id = app_credentials['client_id']
        client_secret = app_credentials['client_secret']
        redirect_url = app_credentials['redirect_url']
        super().__init__(client_id, client_secret, redirect_url, scope=scopes, cache_path='cache/' + username)
        self.username = username

    def response_code2token(self, code: str):
        code = code.strip()
        code = super().parse_response_code(code)
        token = super().get_access_token(code)
        return token


class AsyncSpotify(spotipy.Spotify):
    async def _get(self, url, args=None, payload=None, **kwargs):
        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(None, partial(super()._get(url, args=None, payload=None, **kwargs)))
        return await future

    async def
