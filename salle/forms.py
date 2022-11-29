from django import forms


from API.models import SalleReunion


class CreateSalleForm(forms.Form):
    numero_salle = forms.ModelChoiceField(queryset=SalleReunion.objects.all())
    capacity = forms.IntegerField()


class CreateSalleModelForm(forms.ModelForm):
    class Meta:
        model = SalleReunion
        fields = ['numero_salle', 'capacity']
