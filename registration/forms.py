from django import forms
# from django.core.exceptions import ValidationError
# from django.forms import ModelForm, fields, widgets
from django.urls import reverse_lazy
from django.contrib.auth.forms import (UserCreationForm,PasswordResetForm,SetPasswordForm)
from .models import CustomUser
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit,Layout

class UserForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email address'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'

        self.helper = FormHelper()
        self.helper.form_show_labels = False

        self.helper.form_method = 'post'
        self.helper.form_action = 'register'
        self.helper.layout = Layout( 
            'email',
            'password1',
            'password2'
            )    
        submit = Submit('submit', 'Register')
        submit.field_classes = 'ps-btn ps-btn--fullwidth'
        self.helper.add_input(submit)

    class Meta:
        model = CustomUser
        fields = ('email', 'password1', 'password2')


class UserLoginForm(forms.Form):
    email=forms.EmailField(max_length=256, required=True,widget=forms.EmailInput(attrs={'class': 'form-control', 'name': 'email','placeholder':'Email address'}))
    password=forms.CharField(max_length=128,required=True,widget=forms.PasswordInput(attrs={'class': 'form-control', 'name': 'password','placeholder':'Password'}))


class UserPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(UserPasswordResetForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['placeholder'] = 'Email'


class UserPasswordChangeForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Password'
        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.helper = FormHelper()
        self.helper.form_show_labels = False

        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.layout = Layout( 
            'new_password1',
            'new_password2',
            )    
        submit = Submit('submit', 'CHANGE MY PASSWORD')
        submit.field_classes = 'ps-btn ps-btn--fullwidth'
        self.helper.add_input(submit)
