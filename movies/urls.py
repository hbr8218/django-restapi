from django.urls import path
from . import views


urlpatterns = [
    path('', views.MovieListAPIView.as_view(), name="movies"),
    path('<str:title>', views.MovieDetailListAPIView.as_view(), name="movie-detail"),
    path('add', views.MovieCreateAPIView.as_view(), name="movie_create"),
]
