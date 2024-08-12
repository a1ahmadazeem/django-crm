from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput,TextInput
from .models import Record
from django import forms


class CreateUserForm(UserCreationForm):
    class meta:
        model = User
        fields = ["username","password","password1"]
        
class Loginform (AuthenticationForm):
    username=forms.CharField(widget = TextInput())
    password=forms.CharField(widget = PasswordInput())
    
    
class CreateRecordForm(forms.ModelForm):
    
    class Meta:
        
        model=Record
        fields=['first_name','last_name','email','phone','address','city','province','country']
    
class UpdateRecordForm(forms.ModelForm):
    
    class Meta:
        
        model=Record
        fields=['first_name','last_name','email','phone','address','city','province','country']
    
