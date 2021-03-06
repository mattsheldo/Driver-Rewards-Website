from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm, SetPasswordForm

class UserForm(UserCreationForm):
    prefName = forms.CharField(label='Preferred Name', max_length=128)
    phone = forms.CharField(label='Phone Number', max_length=128)
    address = forms.CharField(label='Address', max_length=128)

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



class UpdatePass(PasswordChangeForm):
    class Meta:
        fields = {'old_password','new_password1','new_password2',}

class UnameForm(forms.Form):
    uname = forms.CharField(label='Username', max_length=128)
    class Meta:
        fields = {'uname'}

class UpdateForm(forms.Form):
    fname = forms.CharField(label='First Name', max_length=128)
    lname = forms.CharField(label='Last Name', max_length=128)
    prefName = forms.CharField(label='Preferred Name', max_length=128)
    email = forms.EmailField(max_length=128)
    phone = forms.CharField(label='Phone Number', max_length=128)
    address = forms.CharField(label='Address', max_length=128)

    class Meta:
        fields = {'fname','lname','prefName','email','phone','address',}


class AlertFilters(forms.Form):
    pointChange = forms.BooleanField(label='Point Change Notifications', initial='True', required=False)
    orderCompletion = forms.BooleanField(label='Order Completion Notifications', initial='True', required=False)
    orderIssue = forms.BooleanField(label='Order Issue Notifications', initial='True', required=False)
    
    class Meta:
        fields = {'pointChange','orderCompletion','orderIssue'}


