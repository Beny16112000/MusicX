from django.shortcuts import render, HttpResponse, redirect
from api.auth import LoginClass
from api.musicRecommendation import Recommendation
from api.playlistGenerator import Generator
from api.songFinder import SongSearch
from api.playlists import Playlists
from django.contrib import messages
import requests
from api.config import Config


# Create your views here.
# Run like this - "python manage.py runserver 8080"


def index(request):
    """
    Home page
    """
    return render(request, 'index.html')



def spotify_login(request):
    """
    Spotify Login
    """
    return LoginClass().redirect_user()



def spotify_callback(request):
    """
    Spotify Callback
    """
    callback = LoginClass().callback(request)
    if callback is not None:
        request.session['access_token'] = callback.access_token
    return redirect('/')



def music_recommendation(request):
    """
    Music recommendation a machine learning algorithm to generate recommendations
    """
    message = ''
    recommendation = Recommendation().tracks()
    if recommendation:
        return render(request, 'recommendation.html',
                                {'recommendation': recommendation})
    else:
        message = 'Dont have recommendation for you sorry !'
        return render(request, 'recommendation.html',
                                {'message': message})




def playlist_generator_choise(request): #playlist_generator
    """
    Generates playlists based on different moods | choise function
    """
    return render(request, 'playlist_generator.html')



def playlist_generator(request):
    """
    Generates playlists based on different moods | result function
    """
    q = request.GET['q']
    gen = Generator(q).generator()
    findId = gen.find("playlist")
    alone = gen[findId:]
    url = f'https://open.spotify.com/playlist/{alone[9:]}'
    return render(request, 'playlist_generator_result.html', {'url': url})



def song_search_results(request):
    """
    Song Search Results
    """
    message = ''
    search = request.GET['search']
    results = SongSearch(search).search()
    if len(results) != 0:
        return render(request, 'search_results.html', {'results': results})
    else:
        message = 'No Results'
        return render(request, 'search_results.html', {'message': message})



def all_playlists(request):
    """
    Client Playlists - Display
    """
    playlists = Playlists().all()
    return render(request, 'all_playlists.html', {'playlists': playlists})



def one_playlist(request, id):
    """
    One playlist - display, detail, share
    """
    single_playlist = Playlists().single_playlist_data(id)
    songs = Playlists().playlist_songs(id)
    return render(request, 'single_playlist.html', {'data': single_playlist,
                                                    'songs': songs})



def logout(request):
    try:
        del request.session['access_token']
        return redirect('/')
    except KeyError:
        messages.error(request, 'Error To Logout')
        return redirect('/')
    
