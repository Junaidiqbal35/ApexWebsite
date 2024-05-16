# forms.py
from django import forms

class TenantContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Full name', 'class': 'input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'input'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Phone number', 'class': 'input'}))
    monthly_budget = forms.DecimalField(max_digits=12, decimal_places=2, widget=forms.NumberInput(attrs={'placeholder': 'Monthly Budget', 'class': 'input'}))
    location_of_interest = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Locations of Interest', 'class': 'input'}))
    property_type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Property Type', 'class': 'input'}))
    bedrooms = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Bedrooms', 'class': 'input'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Comments/Additional Information', 'class': 'input'}), required=False)

    def __init__(self, *args, **kwargs):
        super(TenantContactForm, self).__init__(*args, **kwargs)
        # Iterate over all fields to hide their labels
        for field in self.fields.values():
            field.label = False
