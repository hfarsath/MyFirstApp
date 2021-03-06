from django.db import models
from django.urls import reverse
# Create your models here.
class Album(models.Model):
    Lyricist=models.CharField(max_length=250)
    Album_title=models.CharField(max_length=500)
    Composer=models.CharField(max_length=250)
    Album_logo=models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail',kwargs={'pk':self.pk})
    def __str__(self):
        return self.Album_title 

class Song(models.Model):
    album=models.ForeignKey(Album,on_delete=models.CASCADE)
    song_title=models.CharField(max_length=500)
    is_favorite=models.BooleanField(default=False)
    def __str__(self):
        return self.song_title