from django import forms
from . models import User
from django.shortcuts import get_object_or_404

class FileShareForm(forms.Form):

    username = forms.CharField(label='User you want to share', max_length=127, 
    widget=forms.TextInput(attrs={
        'class':'form-control', 'placeholder': 'Username',
    }))


    def clean_username(self):
        username = self.cleaned_data.get('username')
        user = User.objects.filter(username=username).first()
        if not user:
            raise forms.ValidationError(f'User named {username} doesn\'t exist' )
        return user