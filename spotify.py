from spotipy import oauth2



class SpotifyTokenGetter(oauth2.SpotifyOAuth):
    def __init__(self, app_credentials, username):
        scopes = ' '.join(['playlist-read-private',
                           'playlist-modify-private',
                           'user-library-read',
                           'user-library-modify'
                           ])
        client_id = app_credentials['client_id']
        client_secret = app_credentials['client_secret']
        redirect_url = app_credentials['redirect_url']
        super().__init__(client_id, client_secret, redirect_url, scope=scopes, cache_path='cache/'+username)
        self.username = username

    def response_code2token(self, code):
        code = code.strip()
        code = super().parse_response_code(code)
        token = super().get_access_token(code)
        return token
