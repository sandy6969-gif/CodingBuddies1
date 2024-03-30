from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import Room, User

class MyUserCreationForm(UserCreationForm):
    class Meta:
        model=User
        fields=['name','username','email','password1','password2']


class RoomForm(ModelForm):
    class Meta:
        model=Room
        fields='__all__'
        exclude=['host','participants']
class UserForm(ModelForm):
    class Meta:
        model= User
        fields=['avatar','name','username', 'email','bio']
from django import forms

class ReplyForm(forms.Form):
    # Define the fields for the form here
    # Example:
    # reply = forms.CharField(max_length=100)
    pass
from django import forms
from .models import Message

class MessageForm(forms.ModelForm):
    class Meta:
        model = Message
        fields = ['body']  # Add other fields if needed

        