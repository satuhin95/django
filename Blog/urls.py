
from django.urls import path
from Blog import views

app_name = 'Blog'

urlpatterns = [
    path('', views.BlogList, name='blog_list')
    

]
