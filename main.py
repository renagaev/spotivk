from vk_api import VkApi
from vk import VkUtil
import os
from pprint import pprint
from spotipy.util import prompt_for_user_token

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

