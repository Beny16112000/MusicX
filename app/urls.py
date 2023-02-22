from django.urls import path
from . import views


# Url's

app_name = 'app'

urlpatterns = [
    path('',views.index,name='index'),
    path('login',views.spotify_login,name='spotify_login'),
    path('spotify/callback',views.spotify_callback,name='spotify_callback'),
    path('recommendation',views.music_recommendation,name='music_recommendation'),
    path('playlist/generator',views.playlist_generator_choise,name='playlist_generator_choise'),
    path('playlist/generator/result',views.playlist_generator,name='playlist_generator'),
    path('song/search/',views.song_search_results,name='song_search_results'),
    path('playlists/all',views.all_playlists,name='all_playlists'),
    path('playlists/one/<str:id>',views.one_playlist,name='one_playlist'),
    path('logout',views.logout,name='logout')
]