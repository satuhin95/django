
# from django.conf.urls import url
from django.urls import path
from first_app import views

app_name = "first_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('album/', views.album_list, name='album'),
    path('add-album/', views.add_album, name='add_album'),
    path('add-musician/', views.musician_form, name='musician_form'),

  
]
