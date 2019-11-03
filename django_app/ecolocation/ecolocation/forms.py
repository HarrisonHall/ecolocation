from django import forms
from ecolocation.models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['lat', 'lon', 'start_time', 'end_time', 'radius', 'name']
        widgets = {
            'start_time': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
            'end_time': forms.DateInput(format=('%m/%d/%Y'), attrs={'class':'form-control', 'placeholder':'Select a date', 'type':'date'}),
    }

