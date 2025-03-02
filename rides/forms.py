from django import forms
from rides.models import Person
from datetime import date

class SearchForm(forms.Form):
    origin = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter your city (e.g., Dallas)', 'class': 'form-control'})
    )
    destination_city = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter destination city (e.g., East Rutherford)', 'class': 'form-control'})
    )
    destination_state = forms.CharField(
        required=False,
        widget=forms.TextInput(attrs={'placeholder': 'Enter state code (e.g., NJ)', 'class': 'form-control'})
    )

class RideForm(forms.Form):
  search = forms.CharField(label='Search term', max_length=64, required=False)

class NewRideForm(forms.ModelForm):
    departure_city = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter your departure city',
            'class': 'form-control'
        })
    )
    departure_state = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Enter state (e.g., CA)',
            'class': 'form-control'
        })
    )
    destination_city = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'East Rutherford',
            'class': 'form-control'
        })
    )
    destination_state = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'NJ',
            'class': 'form-control'
        })
    )
    vehicle_type = forms.ChoiceField(
        choices=[
            ('', 'Select vehicle type'),
            ('Sedan', 'Sedan'),
            ('SUV', 'SUV'),
            ('Van', 'Van'),
            ('Truck', 'Truck'),
            ('Electric', 'Electric'),
            ('Hybrid', 'Hybrid'),
            ('Hatchback', 'Hatchback'),
        ],
        widget=forms.Select(attrs={
            'class': 'form-control'
        })
    )
    seats_available = forms.IntegerField(
        min_value=1,
        max_value=8,
        widget=forms.NumberInput(attrs={
            'class': 'form-control',
            'placeholder': 'Number of seats'
        })
    )

    date = forms.DateField(
        required=True,
        widget=forms.DateInput(attrs={
            'type': 'date',
            'class': 'form-control',
            'min': date.today().isoformat()  # Only allow future dates
        })
    )

    time = forms.TimeField(
        required=True,
        widget=forms.TimeInput(attrs={
            'type': 'time',
            'class': 'form-control'
        })
    )

    class Meta:
        model = Person
        fields = ['name', 'email', 'destination_city', 'destination_state', 'date', 'time', 'vehicle_type', 'seats_available']

    def clean(self):
        cleaned_data = super().clean()
        # Add any custom validation here
        return cleaned_data

    def save(self, commit=True):
        instance = super().save(commit=False)
        # Combine the departure city and state into origination
        city = self.cleaned_data.get('departure_city')
        state = self.cleaned_data.get('departure_state')
        instance.origination = f"{city}, {state}"
        if commit:
            instance.save()
        return instance
