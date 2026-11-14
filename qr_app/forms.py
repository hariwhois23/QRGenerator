from django import forms


class QRCodeForm(forms.Form):
    restaurant_name = forms.CharField(max_length=50, label="File Name",
        widget = forms.TextInput(attrs={
            'placeholder': 'Enter File Name',
            'class': 'form-control',}))
    
    menu_url = forms.URLField(max_length=200, label="URL ",
        widget = forms.URLInput(attrs={
            'placeholder': 'Enter URL',
            'class': 'form-control',}))