from django.conf import settings
from django.db import models
from django.urls import reverse

User = settings.AUTH_USER_MODEL


class SalleReunion(models.Model):
    user = models.ForeignKey(User, default=1, null=True,
                             on_delete=models.SET_NULL)
    numero_salle = models.IntegerField(unique=True, blank=False)
    capacity = models.IntegerField(blank=False)

    def __str__(self):
        return str(self.numero_salle)

    def get_absolute_url(self):
        return reverse('salle_details', kwargs={'numero_salle': self.numero_salle})


class Reservation(models.Model):
    id: models.AutoField(auto_created=True, primary_key=True)
    reservation_user = models.ForeignKey(User, default=1, null=True,
                                         on_delete=models.SET_NULL)
    numero_salle = models.ForeignKey(
        SalleReunion, on_delete=models.SET_NULL, null=True)
    reservation_date = models.DateField()
    reservation_time = models.TimeField()
    reservation_duration = models.DurationField()

    def __str__(self):
        return self.numero_salle

    def get_absolute_url(self):
        return reverse('reservation-details', kwargs={'id': self.id})


class User(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    email = models.EmailField(unique=True, max_length=100)
