from turtle import title
from xml.parsers.expat import model
from django.db import models

class Noticia(models.Model):
    title_noticia = models.CharField(max_length=100)
    content_noticia = models.CharField(max_length=200)
    def __str__(self):
        return self.title_noticia