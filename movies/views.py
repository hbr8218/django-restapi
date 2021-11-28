from django.db.models.query import QuerySet
from django.shortcuts import render
from movies.models import Movie
from rest_framework import generics
from .serializers import MovieSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import filters
from rest_framework.response import Response
from django_filters.rest_framework import DjangoFilterBackend


from movies import serializers
# Create your views here.
class MovieListAPIView(generics.ListAPIView):
    serializer_class = MovieSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['id','title','genres','up_votes','down_votes']
    search_fields = ['id','title','genres','up_votes','down_votes']
    ordering_fields = ['id','title','genres','up_votes','down_votes']
    queryset = Movie.objects.all()

### Authenticated
class MovieCreateAPIView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated,]
    serializer_class = MovieSerializer
    queryset = Movie.objects.all()

