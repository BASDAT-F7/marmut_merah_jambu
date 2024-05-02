from django.urls import path
from crud_kelola_album_song.views import show_list_album, show_song_list_album
from crud_kelola_album_song.views import create_song, create_album

app_name = 'crud_kelola_album_song'

urlpatterns = [
    path('', show_list_album, name='show_list_album'),
    path('detail/', show_song_list_album, name='show_song_list_album'),
    path('add-song/', create_song, name='create_song'),
    path('add/', create_album, name='create_album'),
]