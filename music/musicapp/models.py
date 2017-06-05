from django.db import models

# Create your models here.
class MusicCategory(models.Model):
    Genre = models.CharField(max_length=100)

    def __str__(self):
        return self.Genre


class FavoriteSong(models.Model):
    Aritst_Name = models.CharField(max_length=200)
    Song_Name = models.CharField(max_length=100)
    Release_Year = models.DateTimeField(verbose_name='Year song was released')
    Record_Label = models.CharField(max_length=200)
    category = models.ForeignKey(MusicCategory,on_delete= models.CASCADE)

    def __str__(self):
        return self.Song_Name