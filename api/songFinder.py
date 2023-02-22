import spotipy
from spotipy.oauth2 import SpotifyOAuth
from .config import Config


# Song finder system


class SongSearch:
    
    def __init__(self, query):
        self.q = query

    def search(self):
        auth_manager = SpotifyOAuth(
            client_id=f'{Config().clientId()}',
            client_secret=f'{Config().ClientSecret()}',
            redirect_uri='http://localhost:8000/spotify/callback',
            scope=['user-library-read', 'user-read-email', 'user-top-read']
        )

        sp = spotipy.Spotify(auth_manager=auth_manager)
        results = sp.search(q=self.q, type='track', limit=10)

        tracks = []
        for track in results['tracks']['items']:
            tracks.append({
                'name': track['name'],
                'artist': track['artists'][0]['name'],
                'album': track['album']['name'],
                'image': track['album']['images'][0]['url'],
                'id': track['id']
            })

        return tracks
    

