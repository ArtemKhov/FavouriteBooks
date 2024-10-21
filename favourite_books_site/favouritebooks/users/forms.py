from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login*', widget=forms.TextInput())
    password = forms.CharField(label='Password*', widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'password']

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label="Username*", widget=forms.TextInput())
    password1 = forms.CharField(label="Password*", widget=forms.PasswordInput())
    password2 = forms.CharField(label="Repeat password*", widget=forms.PasswordInput())

    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'password1', 'password2']
        labels = {
            'email': 'E-mail*',
        }

        widgets = {
            'email': forms.TextInput(),
        }

    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("This E-mail already exists!")
        return email