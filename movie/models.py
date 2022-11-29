from django.db import models
from datetime import date


class Category(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    url = models.SlugField(max_length=160, unique=True)

    def str(self):
        return self.name

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"


class Actyor(models.Model):
    name = models.CharField(verbose_name="Ismi", max_length=100)
    age = models.PositiveSmallIntegerField(verbose_name="Yoshi", default=0)
    description = models.TextField()
    image = models.ImageField(verbose_name="Rasmi", upload_to='aktyorrasmi/')

    def str(self):
        return self.name

    class Meta:
        verbose_name = "Aktyor va rejissyor"
        verbose_name_plural = "Aktyorlar va rejissyorlar"


class Janr(models.Model):
    name = models.CharField(verbose_name="Janr nomi", max_length=120)
    description = models.TextField()
    slug = models.SlugField(max_length=160, unique=True)

    def str(self):
        return self.name

    class Meta:
        verbose_name = "Janr"
        verbose_name_plural = "Janrlar"


class Kino(models.Model):
    title = models.CharField(verbose_name="Sarlavha", max_length=100)
    tagline = models.CharField(verbose_name="Shiori", max_length=200, default="")
    description = models.TextField(verbose_name="Tavsifi")
    poster = models.ImageField(verbose_name="Plakat rasm", upload_to="kino/")
    year = models.PositiveSmallIntegerField(verbose_name="Ishlab chiqarilish sanasi", default=2021)
    country = models.CharField(verbose_name="Mamlakati", max_length=100)
    directors = models.ManyToManyField(Actyor, verbose_name="Rejissyor", related_name="FilimRahbari")
    actors = models.ManyToManyField(Actyor, verbose_name="Aktyor", related_name="Filimaktyori")
    genres = models.ManyToManyField(Janr, verbose_name="Janiri")
    world_premiers = models.DateField(verbose_name="Jahon primyerasi", default=date.today)
    category = models.ForeignKey(Category, verbose_name="Kategoriya", on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=130, unique=True)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)

    def str(self):
        return self.title

    class Meta:
        verbose_name = "Kino"
        verbose_name_plural = "Kinolar"


class KinoKadrlar(models.Model):
    title = models.CharField(verbose_name="Sarlavha", max_length=120)
    description = models.TextField(verbose_name="Tavsifi")
    image = models.ImageField(verbose_name="Kadr_rasmlari", upload_to="kadrrasmi/")
    movie = models.ForeignKey(Kino, verbose_name="Kino", on_delete=models.CASCADE, blank=True, null=True)

    def str(self):
        return self.title

    class Meta:
        verbose_name = "Film kadiri"
        verbose_name_plural = "Film Kadrlari"


class ReytingYulduzi(models.Model):
    value = models.SmallIntegerField(default=0)

    def str(self):
        return f"{self.value}"

    class Meta:
        verbose_name = "Mashxur reyting"
        verbose_name_plural = "Mashxur reytinglar"
        ordering = ["-value"]


class Reyting(models.Model):
    star = models.ForeignKey(ReytingYulduzi, on_delete=models.CASCADE, verbose_name="Yulduz", blank=True, null=True)
    movie = models.ForeignKey(Kino, on_delete=models.CASCADE, verbose_name="Kino", blank=True, null=True,
                              related_name="retings")

    def str(self):
        return f"{self.star} {self.movie}"

    class Meta:
        verbose_name = "Reyting"
        verbose_name_plural = "Reytinlar"
