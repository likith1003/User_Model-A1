from django import forms
from django.contrib.auth.models import User
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        # fields = '__all__'
        fields = ['first_name', 'last_name', 'email', 'username', 'password']
        help_texts = {'username':''}
