from.models import  *
from django import  forms


class touristform(forms.ModelForm):
    class Meta:
        model=tour_destinations
        fields="__all__"