from django import forms
from API.models import Reservation


class CreateReservationForm(forms.Form):
    numero_salle = forms.ModelChoiceField(queryset=Reservation.objects.all())
    reservation_date = forms.DateField()
    reservation_time = forms.TimeField()
    reservation_duration = forms.DurationField()


class CreateReservationModelForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = [
            'numero_salle',
            'reservation_date',
            'reservation_time',
            'reservation_duration',
            'id',
        ]
