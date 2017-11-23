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
    '''
    некоторые методы spotipy.Spotify в event_loop.run_in_executor()
    '''

    def __init__(self, executor, auth=None, requests_session=True,
                 client_credentials_manager=None, proxies=None, requests_timeout=None):
        super().__init__(self, auth, requests_session,
                         client_credentials_manager, proxies)
        self.loop = asyncio.get_event_loop()
        self.executor = executor

    async def user_playlist_create(self, user, name, public=False):
        func = partial(super().user_playlist_create, user, name, public)
        await self.loop.run_in_executor(self.executor, func)

    async def search(self, q, limit=10, offset=0, type='track', market=None):
        func = partial(super().search, q, limit, offset, type, market)
        return await self.loop.run_in_executor(self.executor, func)

    async def current_user_playlists(self, limit=50, offset=0):
        func = partial(super().current_user_playlists(limit, offset))
        return await self.loop.run_in_executor(self.executor, func)

    async def current_user(self):
        return await self.loop.run_in_executor(self.executor, super().current_user)

