from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

class UserRegistrationForm(forms.Form):
	username = forms.CharField(
                        label="",
                        max_length=100,
                        min_length=5,
                        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
	email = forms.EmailField(
							label="", 
							widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}))
	password = forms.CharField(
                            label="",
                            max_length=100,
                            min_length=5,
                            widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Password'}))
	confirm_password = forms.CharField(
                            label="",
                            max_length=100,
                            min_length=5,
                            widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder': 'Confirm Password'}))

	def clean_email(self):
		email = self.cleaned_data['email']
		qs = User.objects.filter(email=email)
		if qs.exists():
			raise forms.ValidationError('Email is already registered.')
		return email
	
	def clean_username(self):
		username = self.cleaned_data['username']
		qs = User.objects.filter(username=username)
		if qs.exists():
			raise forms.ValidationError('Username has been taken.')
		return username

	def clean_confirm_password(self):
		password = self.cleaned_data['password']
		confirm_password = self.cleaned_data['confirm_password']

		if password and confirm_password and password != confirm_password:
			raise forms.ValidationError('Password fields do not match')
		return confirm_password
