from django.db import models

class Reservation(models.Model):
    STATUS_CHOICES = [('active', 'Active'), ('cancelled', 'Cancelled'), ('completed', 'Completed')]

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    event = models.ForeignKey('events.Event', on_delete=models.CASCADE)
    participant_count = models.IntegerField(default=1)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    reserved_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'reservations'

    def __str__(self):
        return f"{self.user} - {self.event}"