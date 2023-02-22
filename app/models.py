from django.db import models


# Create your models here.


class SpotifyUser(models.Model):
    user_id = models.CharField(max_length=255)
    access_token = models.CharField(max_length=255)
    token_type = models.CharField(max_length=50)
    expires_in = models.IntegerField()
    refresh_token = models.CharField(max_length=255)
    last_login = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'Spotify User'



class ClientId(models.Model):
    client_id = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Client ID'



class ClientSecret(models.Model):
    client_secret = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Client Secret'

