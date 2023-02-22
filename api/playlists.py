import spotipy
from spotipy.oauth2 import SpotifyOAuth
from .config import Config


# Playlists System


class Playlists:

    def all(self):
        auth_manager = SpotifyOAuth(
            client_id=f'{Config().clientId()}',
            client_secret=f'{Config().ClientSecret()}',
            redirect_uri='http://localhost:8000/spotify/callback',
            scope=['user-library-read', 'user-read-email', 'user-top-read']            
        )

        sp = spotipy.Spotify(auth_manager=auth_manager)
        playlists = sp.current_user_playlists()
        data = {
            'playlists': playlists['items']
        }
        return data
    

    def single(self, playlist_id):
        auth_manager = SpotifyOAuth(
            client_id=f'{Config().clientId()}',
            client_secret=f'{Config().ClientSecret()}',
            redirect_uri='http://localhost:8000/spotify/callback',
            scope=['user-library-read', 'user-read-email', 'user-top-read']            
        )

        sp = spotipy.Spotify(auth_manager=auth_manager)
        playlist = sp.playlist(playlist_id)
        return playlist
    

    def single_playlist_data(self, playlist_id):
        playlist = self.single(playlist_id)
        if len(playlist['images']) != 0:
            playlist_name = playlist['name']
            playlist_description = playlist['description']
            playlist_owner = playlist['owner']['display_name']
            playlist_image_url = playlist['images'][0]['url']

            return {
                'playlist_name': playlist_name,
                'playlist_description': playlist_description,
                'playlist_owner': playlist_owner,
                'playlist_image_url': playlist_image_url
            }
        
        else:
            playlist_name = playlist['name']
            playlist_description = playlist['description']
            playlist_owner = playlist['owner']['display_name']

            return {
                'playlist_name': playlist_name,
                'playlist_description': playlist_description,
                'playlist_owner': playlist_owner,
                'playlist_image_url': 0
            }


    def playlist_songs(self, playlist_id):
        playlist = self.single(playlist_id)
        tracks = playlist['tracks']['items']
        songs = []
        for track in tracks:
            track_info = track['track']
            song = {
                'title': track_info['name'],
                'artist': track_info['artists'][0]['name'],
                'album': track_info['album']['name'],
                'image_url': track_info['album']['images'][0]['url'],
                'release_date': track_info['album']['release_date'],
                'url': track_info['external_urls']['spotify']
            }

            songs.append(song)

        return songs


