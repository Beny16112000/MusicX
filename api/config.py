from app.models import ClientId, ClientSecret
import requests

# Config App with Spotify


class Config:

    def clientId(self):
        client_id = ClientId.objects.first()
        return client_id.client_id

    
    def ClientSecret(self):
        client_secret = ClientSecret.objects.first()
        return client_secret.client_secret

    
    def moods(self):
        return {
            'happy': 'spotify:playlist:37i9dQZF1DXdPec7aLTmlC',
            'sad': 'spotify:playlist:37i9dQZF1DWZeKCadgRdKQ',
            'energetic': 'spotify:playlist:37i9dQZF1DX76Wlfdnj7AP',
            'relaxed': 'spotify:playlist:37i9dQZF1DWZeKCadgRdKQ'
        }
    

    def website(self):
        return 'http://localhost:8000/'
    

    def domain(self):
        return 'domain'

