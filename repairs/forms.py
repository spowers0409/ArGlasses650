from django import forms
from .models import Vehicle, RepairType, Repair

class VehicleForm(forms.ModelForm):
    year = forms.ChoiceField(
        choices=[('Select Year', 'Select Year')] + [(year, year) for year in range(1980, 2025)]
    )
    make = forms.ChoiceField(
        choices=[
            ('Select Make', 'Select Make'),
            ('Ford', 'Ford'),
            ('Dodge', 'Dodge'),
            ('Chevrolet', 'Chevrolet')
        ]
    )
    model = forms.ChoiceField(
        choices=[('Select Model', 'Select Model')]
    )
    trim = forms.ChoiceField(
        choices=[('', 'Select Trim')]
    )

    type_of_repair = forms.ChoiceField(
        choices=[
            ('', 'Select Type of Repair'),
            ('Body', 'Body'),
            ('Fuel System', 'Fuel System'),
            ('Engine', 'Engine'),
            ('Transmission', 'Transmission'),
            ('Brake System', 'Brake System'),
            ('Suspension System', 'Suspension System')
        ]
    )
    repair = forms.ChoiceField(
        choices=[('', 'Select Repair')],
        required=False
    )

    class Meta:
        model = Vehicle
        fields = ['year', 'make', 'model', 'trim']

class RepairTypeForm(forms.ModelForm):
    class Meta:
        model = RepairType
        fields = ['name']

class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ['repair_type']
