from django.db import models


# Create your models here.
class AboutParagraph(models.Model):

    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='about/', blank=False)

    def __str__(self):
        return self.title


class YearStats(models.Model):

    year = models.IntegerField()
    salary = models.IntegerField()
    salary_vac = models.IntegerField()
    count = models.IntegerField()
    count_vac = models.IntegerField()

    def __str__(self):
        return str(self.year)


class ImageStat(models.Model):

    name = models.CharField(max_length=20, primary_key=True)
    image = models.ImageField()

    def __str__(self):
        return self.name


class CitySal(models.Model):

    city = models.CharField(max_length=20)
    salary = models.IntegerField()

    def __str__(self):
        return self.city


class CityLevel(models.Model):

    city = models.CharField(max_length=20)
    fraction = models.FloatField()

    def __str__(self):
        return self.city


class Skill(models.Model):

    name = models.CharField(max_length=30)
    year = models.IntegerField()
    count = models.IntegerField()

    def __str__(self):
        return f"{self.year}/{self.name}"
