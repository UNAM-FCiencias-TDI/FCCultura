from django.db import models
from django.utils import timezone
# Create your models here.
# Modelo Post

class Post(models.Model):
    autor = models.Foreignkey('auth.User')
    title = models.CharField(max_length=200)#campo de texto max 200 caracteres
    text = models.TextField()# area de texto
    created_date = models.DateTimeField(
        default = timezone.now)
    published_date = models.DateTimeField(
        blank = True, null = True)

    def publish():
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
