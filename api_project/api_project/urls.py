
from django.contrib import admin
from django.urls import path
from api_example import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
]
