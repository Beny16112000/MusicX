import spotipy
from spotipy.oauth2 import SpotifyOAuth
from .config import Config
from surprise import Dataset, Reader, KNNBasic
import pandas as pd


# Music Recommendation System 

class Recommendation:

    def tracks(self):
        auth_manager = SpotifyOAuth(
        client_id=f'{Config().clientId()}',
        client_secret=f'{Config().ClientSecret()}',
        redirect_uri='http://localhost:8000/spotify/callback',
        scope=['user-library-read', 'user-read-email', 'user-top-read']
    )
        sp = spotipy.Spotify(auth_manager=auth_manager)

        top_tracks = sp.current_user_top_tracks(limit=20, time_range='medium_term')

        track_ids = [track['id'] for track in top_tracks['items']]
        audio_features = sp.audio_features(track_ids)

        df = pd.DataFrame(top_tracks['items'], columns=['id', 'name', 'artists'])
        df['rating'] = 1

        reader = Reader(rating_scale=(0, 1))
        data = Dataset.load_from_df(df[['id', 'name', 'rating']], reader)


        algo = KNNBasic()
        trainset = data.build_full_trainset()
        algo.fit(trainset)

        recommendations = algo.get_neighbors(0, k=10)

        return self.collaborative_filtering(recommendations, df, sp)

    
    def collaborative_filtering(self, recommendations, df, sp):
        if isinstance(recommendations, list) and len(recommendations) > 0:
            recommended_tracks = []
            
            for recommended_track_idx in recommendations:
                recommended_track_id = df.iloc[recommended_track_idx]['id']
                recommended_track = sp.track(str(recommended_track_id))
                
                if recommended_track['album']:
                    album = sp.album(recommended_track['album']['id'])
                    image_url = album['images'][0]['url']
                    recommended_tracks.append({
                        'song_name': recommended_track['name'],
                        'artists': recommended_track['artists'],
                        'album': recommended_track['album']['name'],
                        'image_url': image_url
                    })
            
            return recommended_tracks
        else:
            return False   


