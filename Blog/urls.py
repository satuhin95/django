
from django.urls import path
from Blog import views

app_name = 'Blog'

urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('create/', views.CreateBlog.as_view(), name='create_blog'),
    path('details/<slug>', views.blog_details, name='blog_details'),
    path('liked/<id>', views.liked, name='liked'),
    path('unliked/<id>', views.unliked, name='unliked'),
    path('my-blogs/', views.MyBlogs.as_view(), name='my_blogs'),
    path('edit/<pk>', views.EditBlog.as_view(), name='edit_blog'),
    

]
