from django import forms
from myapp.models import *

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'

class WebpageForm(forms.ModelForm):
    class Meta:
        model=Webpage
        fields=('topic','name','url')#'__all__'
        #exclude=('url',)

from django.contrib.auth.models import User
class UserModelForm(forms.ModelForm):
    password=forms.CharField(max_length=30,widget=forms.PasswordInput)
    class Meta:
        model = User 
        fields = ("username","password","email","is_staff","is_superuser")

