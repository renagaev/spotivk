import asyncio
from vk import VkUtil
import os
import concurrent.futures


# spotify config
username = "rnagaev68"
client_secret = 'a8d084023a60442ebe8e7f60c22143b7'
client_id = '4ccd225f104940fd8c9ee89cb4a76334'
redirect_url = 'http://localhost/'
scopes = ' '.join(['playlist-read-private',
                   'playlist-modify-private',
                   'user-library-read',
                   'user-library-modify'
                   ])

# vk_api config
vk_login = '89622334443'
vk_pass = 'htyfnqaz'

async def consumer(queue: asyncio.Queue):
    num = 1
    while True:
        track = await queue.get()
        if track is None:
            break
        artist = track['artist']
        title = track['title']
        print(f'Track {num}: {artist} --- {title}')
        await asyncio.sleep(0.1)

if __name__ == '__main__':
    if not os.path.exists('cache'):
        os.mkdir('cache')
    me = VkUtil(vk_login, vk_pass)

    loop = asyncio.get_event_loop()
    queue = asyncio.Queue(loop=loop)
    pool = concurrent.futures.ThreadPoolExecutor(max_workers=2)

    alil = asyncio.gather(me.get_music_by_id(79393429, queue, pool), consumer(queue))
    loop.run_until_complete(alil)
    loop.close()
