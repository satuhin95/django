
# from django.conf.urls import url
from django.urls import path
from first_app import views

app_name = "first_app"

urlpatterns = [
    path('', views.IndexView.as_view() , name="index"),
    path('musician-details/<pk>/', views.MusicianDetails.as_view() , name="musician_details"),
    path('musician-add/', views.MusicianCreate.as_view() , name="musician_add"),
    path('musician-update/<pk>/', views.MusicianUpdate.as_view() , name="musician_update"),
    path('musician-delete/<pk>/', views.MusicianDelete.as_view() , name="musician_delete"),
  
]
