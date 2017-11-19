import vk_api
from vk_api.audio import VkAudio
import asyncio


class VkUtil:
    def __init__(self, login, password):
        self.session = vk_api.VkApi(login, password)
        self.api = self.session.get_api()
        self.session.auth()
        self.audio = VkAudio(self.session)

    def get_music(self, vk_id, offset):
        return self.audio.get(vk_id, offset)


    async def get_music_by_id(self, vk_id, event_loop, queue):


        offset = 0
        while True:
            furure = loop.
            audios =
            if not audios:
                break
            buffer.extend(audios)
            offset += len(audios)
            print(len(audios))
        return music

    def link_to_vk_id(self, link):
        short_name = link.split('/')[-1]
        try:
            return self.api.users.get(user_ids=short_name, fields='id')[0]['id']
        except vk_api.exceptions.ApiError:
            try:
                return self.api.groups.getById(group_id=short_name, fields='id')[0]['id']
            except vk_api.exceptions.ApiError:
                return
