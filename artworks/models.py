from django.db import models

class Artist(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True, null=True)
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'artists'

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Artwork(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100, blank=True, null=True)
    image_url = models.URLField(max_length=500, blank=True, null=True)
    view_count = models.IntegerField(default=0)
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)

    class Meta:
        db_table = 'artworks'

    def __str__(self):
        return self.title