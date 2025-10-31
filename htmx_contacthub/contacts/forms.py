from django import forms
from django.contrib.auth import constant_time_compare
from .models import Contact

class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(attrs={
                               'class': "input input-bordered w-full",
                               'placeholder': "Contact Name"
                               })
    )
    
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={
                               'class': "input input-bordered w-full",
                               'placeholder': "Email"
                               })
    )
    
    class Meta:
        model = Contact
        fields = [
            'name', 'email'
        ]