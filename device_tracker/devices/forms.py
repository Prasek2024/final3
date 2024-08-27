from django import forms
from .models import Device


class DeviceForm(forms.ModelForm):
    class Meta:
        model = Device
        fields = ['type', 'vendor', 'serial_number', 'OAM_address', 'date_added']
        widgets = {
            'type': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter device type'}),
            'vendor': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter device vendor'}),
            'date_added': forms.DateInput(
                attrs={'class': 'form-control', 'placeholder': 'Select publication date', 'type': 'date'}),
            'OAM_address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter OAM address'}),

        }


class DeviceSearchForm(forms.Form):
    device_name = forms.CharField(
        label='Device name',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Search for a device'})
    )