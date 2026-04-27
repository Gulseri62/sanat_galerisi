from django.db import models

class Order(models.Model):
    STATUS_CHOICES = [('pending', 'Pending'), ('confirmed', 'Confirmed'), ('shipped', 'Shipped'), ('delivered', 'Delivered'), ('cancelled', 'Cancelled')]

    user = models.ForeignKey('users.User', on_delete=models.CASCADE)
    artwork = models.ForeignKey('artworks.Artwork', on_delete=models.CASCADE)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    ordered_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.user}"

class Payment(models.Model):
    METHOD_CHOICES = [('credit_card', 'Credit Card'), ('debit_card', 'Debit Card'), ('bank_transfer', 'Bank Transfer')]

    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)
    reservation = models.ForeignKey('reservations.Reservation', on_delete=models.SET_NULL, null=True, blank=True)
    method = models.CharField(max_length=20, choices=METHOD_CHOICES)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    paid_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Payment {self.id}"

class Coupon(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_rate = models.DecimalField(max_digits=5, decimal_places=2)
    valid_until = models.DateField()
    user = models.ForeignKey('users.User', on_delete=models.SET_NULL, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.code