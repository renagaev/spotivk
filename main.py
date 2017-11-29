import asyncio
import concurrent.futures
import os
import re

from spotipy.oauth2 import SpotifyClientCredentials

from spotify import SpotifyTokenGetter, AsyncSpotify
from vk import VkUtil

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
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=5)

    me_vk = VkUtil(login=vk_login, password=vk_pass, executor=pool)
    token = SpotifyTokenGetter(app, 'rnagaev68').get_cached_token()
    me_sp = AsyncSpotify(pool, auth=token["access_token"], client_credentials_manager=app2)


    async def search(track):

        track_q = '{} {}'.format(track['artist'], track['title'])
        track_q = re.sub(r'([^\s\w]|_)+', '', track_q)
        result = await me_sp.search_track(track_q)
        if result:
            return result[0]


    async def get_tracks_from_queue(queue):
        tracks = []
        while True:
            track = await queue.get()

            if track is None or queue.qsize() <= 1:
                break
            else:
                tracks.append(track)
        return tracks


    async def main(queue):
        al = 0
        fi = 0
        while True:
            tracks = await get_tracks_from_queue(queue)
            al += len(tracks)
            if tracks:
                futures = [search(track) for track in tracks]
            else:
                asyncio.sleep(1)
                continue

            for i in await asyncio.gather(*futures):
                if i:
                    fi += 1
                    print(f'{fi} из {al}')


    loop.run_until_complete(asyncio.gather(main(queue), me_vk.get_music_by_id(154622421, queue)))
    loop.close()
