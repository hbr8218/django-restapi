from django.urls import path
from .views import RegisterView, LoginView, UserCreateFavGenreAPIView


urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('fav_genre',UserCreateFavGenreAPIView.as_view()),
]
