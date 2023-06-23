
from django.urls import path
from App_Login import views


app_name ='App_Login'
urlpatterns = [
    path('signup/', views.sign_up , name="sign_up"),
    path('login/', views.login_page , name="login_page"),
    path('logout/', views.logout_user , name="logout_user"),
    path('profile/', views.user_profile , name="user_profile"),
    path('profile-change/', views.user_change , name="user_change"),
    path('password-change/', views.password_change , name="password_change"),
    path('profile-picture/', views.profile_change , name="profile_change"),
    path('profile-picture-change/', views.change_profile_pic , name="change_profile_pic"),

]

