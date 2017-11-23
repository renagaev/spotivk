import vk_api
from vk_api.audio import VkAudio
import asyncio
from functools import partial
import concurrent.futures


class VkUtil:
    def __init__(self, login: str, password: str, executor):
        self.session = vk_api.VkApi(login, password)
        self.api = self.session.get_api()
        self.session.auth()
        self.audio = VkAudio(self.session)
        self.executor = executor

    async def get_music_by_id(self, vk_id: int, queue: asyncio.Queue):
        loop = asyncio.get_event_loop()
        offset = 0
        while True:
            future = loop.run_in_executor(self.executor, partial(self.audio.get, owner_id=vk_id, offset=offset))
            music = await future
            if not music:
                break

            for i in music:
                await queue.put(i)

            print(queue.qsize())
            offset += len(music)

        queue.put(None)

    async def link_to_vk_id(self, link):

        loop = asyncio.get_event_loop()
        short_name = link.split('/')[-1]

        try:
            response = await loop.run_in_executor(self.executor,
                                                  partial(self.api.groups.getById, group_id=short_name, fields='id'))
            return response[0]['id']
        except vk_api.exceptions.ApiError:
            try:
                response = await loop.run_in_executor(self.executor,
                                                      partial(self.api.users.get, user_ids=short_name, fields='id'))
                return response[0]['id']
            except vk_api.exceptions.ApiError:
                return
