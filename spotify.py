import spotipy
from spotipy import oauth2
import json

class SpotifyUtils(oauth2.SpotifyOAuth):

    def __init__(self, app_credentials):
        self.cache_path = 'cache/'
        scopes = ' '.join(['playlist-read-private',
                          'playlist-modify-private',
                          'user-library-read',
                          'user-library-modify'
                          ])
        client_id = app_credentials['client_id']
        client_secret = app_credentials['client_secret']
        redirect_url = app_credentials['redirect_url']
        super().__init__(client_id, client_secret, redirect_url, scope=scopes)

    def get_token_from_cache(self, username):
        ''' Gets a cached auth token
        '''
        path = self.cache_path
        self.cache_path += username
        token = super().get_cached_token()
        self.cache_path = path
        return token

    def response_code2token(self, code):
        code = super().parse_response_code(code)
        token = super().get_access_token(code)
        return token

