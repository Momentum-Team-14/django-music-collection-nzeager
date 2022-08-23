from xml.dom.minidom import AttributeList
from django.db import models


class Album(models.Model):
    title = models.CharField(max_length=200)
    artist = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.title} by {self.artist}'
