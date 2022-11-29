from rest_framework import serializers
from .models import Category, Actyor, Janr, Kino, KinoKadrlar, ReytingYulduzi, Reyting


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ActyorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actyor
        fields = '__all__'


class JanrSerializer(serializers.ModelSerializer):
    class Meta:
        model = Janr
        fields = '__all__'


class KinoSerializer(serializers.ModelSerializer):
    directors = ActyorSerializer()
    actors = ActyorSerializer()
    genres = JanrSerializer()
    category = CategorySerializer()

    class Meta:
        model = Kino
        fields = ('id', 'title', 'tagline', 'description', 'poster', 'year', 'country', 'directors', 'actors', 'genres',
                  'category', 'world_premiers', 'slug', 'like', 'dislike')


class KinoKadrlarSerializer(serializers.ModelSerializer):
    movie = KinoSerializer()

    class Meta:
        model = KinoKadrlar
        fields = ('id', 'movie', 'title', 'description', ' image')


class ReytingYulduziSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReytingYulduzi
        fields = '__all__'


class ReytingSeializer(serializers.ModelSerializer):
    # star = ReytingYulduziSerializer(many=False, write_only=True)
    # movie = KinoSerializer(many=False, write_only=True)

    class Meta:
        model = Reyting
        fields = ("id", "star", "movie")
