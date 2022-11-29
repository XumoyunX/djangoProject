import django_filters
from django.shortcuts import render
from .serializers import CategorySerializer, ActyorSerializer, JanrSerializer, KinoSerializer, KinoKadrlarSerializer, \
    ReytingYulduziSerializer, ReytingSeializer
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView
from .models import *


class CategoryView(ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class CategoryDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ActorView(ListCreateAPIView):
    queryset = Actyor.objects.all()
    serializer_class = ActyorSerializer


class ActorDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Actyor.objects.all()
    serializer_class = ActyorSerializer


class JanrView(ListCreateAPIView):
    queryset = Janr.objects.all()
    serializer_class = JanrSerializer


class JanrDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Janr.objects.all()
    serializer_class = JanrSerializer


class MovieView(ListCreateAPIView):
    queryset = Kino.objects.prefetch_related("directors", 'actors', 'genres').select_related()
    serializer_class = KinoSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['category', 'like', 'title', 'directors','actors', 'genres']


class MovieDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Kino.objects.prefetch_related("directors", 'actors', 'genres').select_related('category')
    serializer_class = KinoSerializer


class KinoKadrView(ListCreateAPIView):
    queryset = KinoKadrlar.objects.select_related('movie').order_by('-id')
    serializer_class = KinoKadrlarSerializer


class KinoKadrDetailView(ListCreateAPIView):
    queryset = KinoKadrlar.objects.select_related('movie').order_by('-id')
    serializer_class = KinoKadrlarSerializer


class ReytingYulduziView(ListCreateAPIView):
    queryset = ReytingYulduzi.objects.all()
    serializer_class = ReytingYulduziSerializer


class ReytingYulduziDetailView(RetrieveUpdateDestroyAPIView):
    queryset = ReytingYulduzi.objects.all()
    serializer_class = ReytingYulduziSerializer


class ReytingView(ListCreateAPIView):
    queryset = Reyting.objects.select_related("star", "movie")
    serializer_class = ReytingSeializer


class ReytingDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Reyting.objects.select_related("star", "movie")
    serializer_class = ReytingSeializer


