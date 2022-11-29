from django.urls import path
from .views import *
urlpatterns = [
    path('category/', CategoryView.as_view()),
    path('category/<int:pk>/', CategoryDetailView.as_view()),
    path('actor', ActorView.as_view()),
    path('actor/<int:pk>/', ActorDetailView.as_view()),
    path('janr/', JanrView.as_view()),
    path('janr/<int:pk>/', JanrView.as_view()),
    path('movie/', MovieView.as_view()),
    path('movie/<int:pk>/', MovieDetailView.as_view()),
    path('kinokadr/', KinoKadrView.as_view()),
    path('kinokadr/<int:pk>/', KinoKadrDetailView.as_view()),
    path('reyting/', ReytingYulduziView.as_view()),
    path('reyting/<int:pk>/', ReytingYulduziDetailView.as_view()),

]