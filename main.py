from vk_api import VkApi
import os
import spotify
import spotipy


username = "rnagaev68"
app = { 'client_secret': 'a8d084023a60442ebe8e7f60c22143b7',
        'client_id': '4ccd225f104940fd8c9ee89cb4a76334',
        'redirect_url': 'https://vk.com/feed'}



def main():
    if not os.path.exists('cache'):
        os.mkdir('cache')

    token_or_url = spotify.generate_token_url(username, app)
    print(token_or_url)
    url = input()
    if not token_or_url.get('token'):
        token = spotify.parse_token_url(token_or_url, username, app)
    else:
        token = token_or_url['token']

    me = spotipy.Spotify(auth=token)
    me.user_playlist_create('rnagaev68', 'from api', public=False)




if __name__ == '__main__':
    main()