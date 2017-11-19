from vk_api import VkApi
from vk import VkUtil
import os
from pprint import pprint
from spotipy import Spotify

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

if __name__ == '__main__':
    if not os.path.exists('cache'):
        os.mkdir('cache')
    import vk_api  # learn more: https://python.org/pypi/vk_api
    import asyncio

    login = '89622334443'
    password = 'htyfnqaz'
    session = vk_api.VkApi(login, password)
    session.auth()
    audio = vk_api.audio.VkAudio(session)




    async def get_all_music(vk_id, loop, buff):
        offset = 0
        while True:
            music = await audio.get(owner_id=vk_id, offset=offset)

            if music:
                is_done = True
                break
            buff.extend(music)
            offset += len(music)
            print(len(buff))


    async def print_buff(buff):
        while True:
            if buff:
                async for _ in buff:
                    a = buff.pop()
                    pprint(str(len(buff)) + 'audios in buffer. Last =' + a['title'])
            else:
                if is_done:
                    break
                else:
                    asyncio.sleep(1)


    async def main():
        buffe = []
        coroutines = [get_all_music(183116683, buffe), print_buff(buffe)]
        completed, pending = await asyncio.wait(coroutines)


    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.run_in_executor()
