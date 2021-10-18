from django import forms
from django.contrib import messages
from django.contrib.auth import get_user_model


non_allowed_usernames = ['bad_word']

User = get_user_model()

messages = {
	'required':'required',
	'invalid':'invalid',
	'max_length':'max_length',
}

class RegisterForm(forms.Form):
    username = forms.CharField(error_messages=messages, max_length=30, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    email = forms.EmailField(error_messages=messages, max_length=50, widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Email'}))
    password = forms.CharField(error_messages=messages, max_length=40, widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

    def clean_username(self):
        username = self.cleaned_data.get("username")
        qs = User.objects.filter(username__iexact=username)
        if username in non_allowed_usernames:
            raise forms.ValidationError("Invalid Usename.")
        if qs.exists():
            raise forms.ValidationError("Invalid Usename.")
        return username
    
    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("This email is already in use.")
        return email
