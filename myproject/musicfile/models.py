from django.db import models
from django.urls import reverse

class Album(models.Model):
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=250)
    region = models.CharField(max_length=250)
    logo = models.ImageField(upload_to='album_pic',blank=True)

    # to show correct in list view without showing object name in admin page
    def __str__(self):
        return self.album_title

    def get_absolute_url(self):
        return reverse('musicfile:DetailOfAlbums', kwargs={'pk': self.pk})



class Songs(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=250)
    song_title = models.CharField(max_length=250)
    is_favourite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title
