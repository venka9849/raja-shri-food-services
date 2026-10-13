from django.db import models

# Create your models here.
class MenuItems(models.Model):
    Item_name = models.CharField(max_length=100)
    Price = models.DecimalField(max_digits=8,decimal_places=2)
    discription = models.TextField(blank=True)
    image = models.ImageField(upload_to='menu_images/', blank=True, null=True)
    is_available = models.BooleanField(default=True)


class BusinessHours(models.Model):
    DAY_CHOICES = [
        ('Monday', 'Monday'),
        ('Tuesday', 'Tuesday'),
        ('Wednesday', 'Wednesday'),
        ('Thursday', 'Thursday'),
        ('Friday', 'Friday'),
        ('Saturday', 'Saturday'),
        ('Sunday', 'Sunday'),
    ]
    day = models.CharField(max_length=10, choices=DAY_CHOICES, unique=True)
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    is_closed = models.BooleanField(default=False)

class BusinessSettings(models.Model):
    phone_number = models.CharField(max_length=15)
    whatsapp_number = models.CharField(max_length=15)