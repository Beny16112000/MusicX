import spotipy
from spotipy.oauth2 import SpotifyOAuth
from django.shortcuts import redirect
from .config import Config
from app.models import SpotifyUser


# Spotify Authentication


class LoginClass:

    def login(self):
        sp_oauth = SpotifyOAuth(
            client_id=f'{Config().clientId()}',
            client_secret=f'{Config().ClientSecret()}',
            redirect_uri='http://localhost:8000/spotify/callback',
            scope=['user-library-read', 'user-read-email']
        )
        
        return sp_oauth


    def redirect_user(self):
        sp_oauth = self.login()
        auth_url = sp_oauth.get_authorize_url()
        return redirect(auth_url)


    def callback(self ,request):
        if request.user.is_authenticated:
            return redirect('/')
        else:
            auth_manager = SpotifyOAuth(requests_session=request, client_id=Config().clientId(), client_secret=Config().ClientSecret(),
                                        redirect_uri='http://localhost:8000/spotify/callback', scope=['user-library-read', 'user-read-email'])

            if not auth_manager.validate_token(auth_manager.get_cached_token()):
                auth_manager.get_access_token(request.GET.get('code'))

            spotify = spotipy.Spotify(auth_manager=auth_manager)
            user_info = spotify.current_user()
            user_id = user_info['id']
            access_token = auth_manager.get_access_token()['access_token']
            token_type = auth_manager.get_access_token()['token_type']
            expires_in = auth_manager.get_access_token()['expires_in']
            refresh_token = auth_manager.get_access_token()['refresh_token']
            spotify_user, created = SpotifyUser.objects.update_or_create(
                user_id = user_id,
                defaults = {
                    'access_token': access_token,
                    'token_type': token_type,
                    'expires_in': expires_in,
                    'refresh_token': refresh_token
                }
            )

            return spotify_user


    def user(self, request):
        spotify_user_id = request.session.get('access_token')
        if spotify_user_id:
            spotify_user = SpotifyUser.objects.get(user_id=spotify_user_id)
            return spotify_user
        

