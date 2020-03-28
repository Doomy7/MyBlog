from django import forms
from django.contrib.auth.forms import UserCreationForm

#custom user registration form, extendes existed form
class UserRegisterForm(UserCreationForm):
    username = forms.CharField(max_length=30)
    email = forms.EmailField()
    Date_of_birth = forms.DateField(widget=forms.widgets.DateInput(attrs={'type': 'date'}))
    phone = forms.IntegerField(max_value=6999999999)
    music = forms.BooleanField(required=False)
    games = forms.BooleanField(required=False)
    arts = forms.BooleanField(required=False)
    movies = forms.BooleanField(required=False)
    bio = forms.CharField(widget=forms.Textarea, max_length=200)

#user login form
class UserLoginForm(forms.Form):
    username = forms.CharField(max_length=100)
    password = forms.CharField(max_length=100, widget=forms.PasswordInput)

#article registration form
class ArticleRegisterForm(forms.Form):
    title = forms.CharField(max_length=50)
    details = forms.CharField(widget=forms.Textarea, max_length=1000)
    music = forms.BooleanField(required=False)
    games = forms.BooleanField(required=False)
    arts = forms.BooleanField(required=False)
    movies = forms.BooleanField(required=False)