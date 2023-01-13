from django.db import models


# Create your models here.
class AboutParagraph(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    image = models.ImageField(upload_to='about/', blank=False)

    def __str__(self):
        return self.title