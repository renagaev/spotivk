import vk_api
from vk_api.audio import VkAudio
import asyncio


class VkUtil:
    def __init__(self, login, password):
        self.session = vk_api.VkApi(login, password)
        self.api = self.session.get_api()
        self.session.auth()
        self.audio = VkAudio(self.session)




    async def get_music_by_id(self, vk_id: int, queue: asyncio.Queue):
        loop = asyncio.get_event_loop()
        offset = 0
        while True:
            future = loop.run_in_executor(None, self.audio.get, vk_id, offset)
            music = await future
            if not music:
                break
            queue.put(music)
            offset += len(music)

        queue.put(None)


    async def link_to_vk_id(self, link):

        loop = asyncio.get_event_loop()
        short_name = link.split('/')[-1]

        def get_user_id():
            return self.api.users.get(user_ids=short_name, fields='id')[0]['id']
        def get_group_id():
            return self.api.groups.getById(group_id=short_name, fields='id')[0]['id']

        try:
            return await loop.run_in_executor(None, get_user_id)
        except vk_api.exceptions.ApiError:
            try:
                return await loop.run_in_executor(None, get_group_id)
            except vk_api.exceptions.ApiError:
                return
