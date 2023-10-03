from django.urls import path,include
from knox import views as knox_views
from .api import RegisterAPI, LoginAPI, UserAPI, ChangePasswordAPI

urlpatterns =[
    path('api/auth',include('knox.urls')),
    path('api/auth/register', RegisterAPI.as_view()),
    path('api/auth', LoginAPI.as_view()),
    path('api/auth', UserAPI.as_views()),

]