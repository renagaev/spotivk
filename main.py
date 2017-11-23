import asyncio
from vk import VkUtil
import os
import concurrent.futures
from spotify import SpotifyTokenGetter, AsyncSpotify
from spotipy.oauth2 import SpotifyClientCredentials
from pprint import pprint

# spotify config
app = dict(
    client_secret='a8d084023a60442ebe8e7f60c22143b7',
    client_id='4ccd225f104940fd8c9ee89cb4a76334',
    redirect_url='http://localhost/')

app2 = SpotifyClientCredentials(client_secret='a8d084023a60442ebe8e7f60c22143b7',
                                client_id='4ccd225f104940fd8c9ee89cb4a76334')

scopes = ' '.join(['playlist-read-private',
                   'playlist-modify-private',
                   'user-library-read',
                   'user-library-modify'
                   ])
username = "rnagaev68"

# vk_api config
vk_login = '89622334443'
vk_pass = 'htyfnqaz'


if True:
    if not os.path.exists('cache'):
        os.mkdir('cache')
    # me = VkUtil(vk_login, vk_pass)

    loop = asyncio.get_event_loop()
    queue = asyncio.Queue(loop=loop)
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=4)
    async def main():
        sp = SpotifyTokenGetter(app, username)
        token = sp.get_cached_token()
        me = AsyncSpotify(pool, auth=token['access_token'], client_credentials_manager=app2)
        pprint(await me.current_user_playlists())

    loop.run_until_complete(main())
    loop.close()


