from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Movie(models.Model):
    title = models.CharField(max_length=200)
    image1 = models.CharField(max_length=500)
    image2 = models.CharField(max_length=500)
    year = models.PositiveIntegerField(default=2025)
    genre = models.CharField(max_length=100)
    time = models.CharField(max_length=10)  # e.g., "2h 10m"
    rate = models.FloatField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    description = models.TextField()
    
    def __str__(self):
        return self.title
    

class Show(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='shows')
    date = models.DateField()
    time = models.TimeField()

    def __str__(self):
        return f"{self.movie.title} - {self.date} at {self.time}"
    

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    show_date = models.DateField()
    show_time = models.TimeField()
    price = models.IntegerField(default=15)
    selected_seats = models.CharField(max_length=200)  # e.g., "A1,A2,B3"
    payment_method = models.CharField(max_length=50, default='UPI')  # NEW
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.username} - {self.movie.title} ({self.show_date} {self.show_time}) - {self.selected_seats}"

