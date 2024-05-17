# forms.py
from django import forms

class TenantContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Full name', 'class': 'input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'input'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Phone number', 'class': 'input'}))
    monthly_budget = forms.CharField(max_length=100,
                                     widget=forms.TextInput(attrs={'placeholder': 'Monthly Budget £200', 'class': 'input'}))
    location_of_interest = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Locations of Interest', 'class': 'input'}))
    property_type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Property Type', 'class': 'input'}))
    bedrooms = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Bedrooms', 'class': 'input'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Comments/Additional Information', 'class': 'input'}), required=False)

    def __init__(self, *args, **kwargs):
        super(TenantContactForm, self).__init__(*args, **kwargs)
        # Iterate over all fields to modify their widget classes
        for field_name, field in self.fields.items():
            # css_classes = field.widget.attrs.get('class', '')
            # field.widget.attrs['class'] = css_classes + ' input-container ic2'
            field.label = False



class LandLordContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Full name', 'class': 'input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'input'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Phone number', 'class': 'input'}))
    monthly_rent = forms.CharField(max_length=100,
                                     widget=forms.TextInput(attrs={'placeholder': 'Monthly Rent £500', 'class': 'input'}))
    address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'input'}))
    property_type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Property Type', 'class': 'input'}))
    bedrooms = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Bedrooms', 'class': 'input'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Comments/Additional Information', 'class': 'input'}), required=False)

    def __init__(self, *args, **kwargs):
        super(LandLordContactForm, self).__init__(*args, **kwargs)
        # Iterate over all fields to hide their labels
        for field in self.fields.values():
            field.label = False


class SellerContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Full name', 'class': 'input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'input'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Phone number', 'class': 'input'}))
    address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'input'}))
    city = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'input'}))
    property_type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Property Type', 'class': 'input'}))
    bedrooms = forms.IntegerField(min_value=0, widget=forms.NumberInput(attrs={'placeholder': 'Bedrooms', 'class': 'input'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Comments/Additional Information', 'class': 'input'}), required=False)

    def __init__(self, *args, **kwargs):
        super(SellerContactForm, self).__init__(*args, **kwargs)
        # Iterate over all fields to hide their labels
        for field in self.fields.values():
            field.label = False


class InvestmentContactForm(forms.Form):
    full_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Full name', 'class': 'input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'input'}))
    phone_number = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Phone number', 'class': 'input'}))
    address = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'input'}))
    city = forms.CharField(max_length=200, widget=forms.TextInput(attrs={'placeholder': 'City', 'class': 'input'}))
    property_type = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'placeholder': 'Property Type', 'class': 'input'}))
    comment = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Comments/Additional Information', 'class': 'input'}), required=False)

    def __init__(self, *args, **kwargs):
        super(InvestmentContactForm, self).__init__(*args, **kwargs)
        # Iterate over all fields to hide their labels
        for field in self.fields.values():
            field.label = False