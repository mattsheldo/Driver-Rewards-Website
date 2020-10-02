from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserForm(UserCreationForm):
    prefName = forms.CharField(max_length=128)
    phone = forms.CharField(max_length=128)
    address = forms.CharField(max_length=128)

    DRIVER = 'DR'
    SPONSOR = 'SP'
    ADMIN = 'AD'
    TYPE_OF_USER_CHOICES = (
    (DRIVER, 'Driver'),
    (SPONSOR, 'Sponsor'),
    (ADMIN, 'Admin'),
    )
    type_of_user_choices = forms.ChoiceField(choices = TYPE_OF_USER_CHOICES)

    class Meta:
        model = User
        fields = ('username','email','password1','password2','first_name','last_name','prefName','phone','address','type_of_user_choices',)

