from spotipy.oauth2 import SpotifyOAuth
import spotipy
from .config import Config



# Playlist Generator by mood System 


class Generator:

    def __init__(self, mood):
        self.mood = mood

    def generator(self):
        auth_manager = SpotifyOAuth(
        client_id=f'{Config().clientId()}',
        client_secret=f'{Config().ClientSecret()}',
        redirect_uri='http://localhost:8000/spotify/callback',
        scope=['user-library-read', 'playlist-modify-public']
    )
        
        sp = spotipy.Spotify(auth_manager=auth_manager)

        recommendations = sp.recommendations(seed_genres=['pop'], limit=10)

        user_id = sp.me()['id']
        playlist_name = f"{self.mood} Playlist"
        playlist_description = f"A {self.mood} playlist"
        playlist = sp.user_playlist_create(user_id, playlist_name, public=True, description=playlist_description)

        tracks = []
        for track in recommendations['tracks']:
            track_dict = {}
            track_dict['name'] = track['name']
            track_dict['artists'] = [artist['name'] for artist in track['artists']]
            track_dict['album'] = track['album']['name']
            track_dict['image_url'] = track['album']['images'][0]['url']
            tracks.append(track_dict)

        tracks_ids = [track['id'] for track in recommendations['tracks']]
        sp.user_playlist_add_tracks(user_id, playlist['id'], tracks_ids)

        user_info = sp.current_user()
        username = user_info['id']
        playlist_uri = playlist['uri']
        playlist_url = f'spotify:user:{username}:playlist:{playlist_uri.split(":")[-1]}'

        return playlist_url


