from django.db import models

class Review(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    artwork = models.ForeignKey('artworks.Artwork', on_delete=models.SET_NULL, null=True, blank=True)
    event = models.ForeignKey('events.Event', on_delete=models.SET_NULL, null=True, blank=True)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    helpful_votes = models.IntegerField(default=0)
    reply = models.TextField(blank=True, null=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reviews'

    def __str__(self):
        return f"Review {self.id} by {self.user}"

class Favorite(models.Model):
    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    artwork = models.ForeignKey('artworks.Artwork', on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'favorites'
        unique_together = ('user', 'artwork')

    def __str__(self):
        return f"{self.user} - {self.artwork}"

class SupportTicket(models.Model):
    STATUS_CHOICES = [('open', 'Open'), ('in_progress', 'In Progress'), ('closed', 'Closed')]

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'support_tickets'

    def __str__(self):
        return f"{self.subject} - {self.user}"

class Comparison(models.Model):
    ITEM_CHOICES = [('artwork', 'Artwork'), ('event', 'Event')]

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    item_type = models.CharField(max_length=10, choices=ITEM_CHOICES)
    item_ids = models.CharField(max_length=255)
    saved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'comparisons'

    def __str__(self):
        return f"Comparison {self.id} by {self.user}"