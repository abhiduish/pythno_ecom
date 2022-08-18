from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import OtpProfile
# class NameForm(forms.Form):
#     your_name = forms.CharField(label='Your name', max_length=100)

class SignUpForm(UserCreationForm):
	name = forms.CharField(label = ("Full Name"))
	username = forms.EmailField(label = ("Email"))

	class Meta:
		model = User
		fields = ('name', 'username', 'password1', 'password2')