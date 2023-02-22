from django.contrib import admin
from .models import ClientId, ClientSecret, SpotifyUser


# Register your models here.


admin.site.register(ClientId)
admin.site.register(ClientSecret)
admin.site.register(SpotifyUser)