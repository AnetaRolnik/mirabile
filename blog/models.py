from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.TextField(verbose_name='Opis')
    photo = models.ImageField(verbose_name='Zdjęcie', upload_to='img')
    created_date = models.DateTimeField(
            default=timezone.now, verbose_name='Utworzono')
    published_date = models.DateTimeField(
            blank=True, null=True, verbose_name='Data publikacji')

    def publish(self):
        self.save()

    def __str__(self):
        return self.title