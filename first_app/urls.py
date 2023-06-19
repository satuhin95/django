
# from django.conf.urls import url
from django.urls import path
from first_app import views

app_name = "first_app"

urlpatterns = [
    path('', views.index, name='index'),
    path('album/', views.album_list, name='album'),
    path('add-album/', views.add_album, name='add_album'),
    path('add-musician/', views.musician_form, name='musician_form'),
    path('musician-details/<int:id>/', views.musician_details, name='musician_details'),
    path('musician-edit/<int:id>/', views.musician_edit, name='musician_edit'),
    path('musician-delete/<int:id>/', views.musician_delete, name='musician_delete'),
    path('album-edit/<int:id>/', views.album_edit, name='album_edit'),
    path('album-delete/<int:id>/', views.album_delete, name='album_delete'),

  
]
