from django.db import models

# Create your models here.
class Reservation(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    table_number = models.IntegerField()
    reservation_date = models.DateField()
    message = models.TextField()

    def __str__(self):
        return self.name
