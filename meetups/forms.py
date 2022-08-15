from django import forms


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(label='Your email')
