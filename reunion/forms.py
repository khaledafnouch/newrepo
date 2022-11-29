from django import forms


class CreateSalleForm(forms.Form):
    numero_salle = forms.IntegerField()
    capacity = forms.IntegerField()


class ReservationForm(forms.Form):
    reservation_date = forms.DateField(
        widget=forms.SelectDateWidget(empty_label="Not set", months=None)
    )
