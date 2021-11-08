from django import forms
from django.contrib.auth.forms import (AuthenticationForm, PasswordResetForm,
                                       SetPasswordForm)
from django.utils.translation import gettext_lazy as _

from customer.models import UserBase


class UserLoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control mb-3',
               'placeholder': 'Username',
               'id': 'login-username'
               }
    ))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'Password',
            'id': 'login-pwd',
        }
    ))


class RegistrationForm(forms.ModelForm):
    user_name = forms.CharField(label=_('Enter Username'), min_length=4, max_length=50, help_text=_('Requierd'))
    email = forms.EmailField(max_length=100, help_text=_('Required'),
                             error_messages={'required': _('you need an email')})
    password = forms.CharField(label=_('Password'), widget=forms.PasswordInput)
    password2 = forms.CharField(label=_('Repeat Password'), widget=forms.PasswordInput)

    class Meta:
        model = UserBase
        fields = ('user_name', 'email')

    def clean_username(self):
        user_name = self.cleaned_data['user_name'].lower()
        x = UserBase.objects.filter(user_name=user_name)
        if x.count():
            raise forms.ValidationError(_("Username already exists"))
        return user_name

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError(_('Passwords do not match.'))
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if UserBase.objects.filter(email=email).exists():
            raise forms.ValidationError(_('please use another email, already taken'))
        return email

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Username'})
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'E-mail', 'name': 'email', 'id': 'id_email'})
        self.fields['password'].widget.attrs.update(
            {'class': 'form-control mb-3', 'placeholder': 'Password'})
        self.fields['password2'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Repeat Password'})


class UserEditForm(forms.ModelForm):
    email = forms.EmailField(
        label='_(Account email (can not be changed))', max_length=200, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'email', 'id': 'form-email', 'readonly': 'readonly'}))

    user_name = forms.CharField(
        label='Username', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Username', 'id': 'form-username',
                   'readonly': 'readonly'}))

    first_name = forms.CharField(
        label='first_name', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Firstname', 'id': 'form-firstname'}))

    last_name = forms.CharField(
        label='last_name', min_length=4, max_length=50, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Lastname', 'id': 'form-lastname'}))

    phone_number = forms.CharField(
        label='Phone_number', max_length=12, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Phone_number', 'id': 'form-phonenumber'}))

    postcode = forms.CharField(
        label='postcode', max_length=20, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Postcode', 'id': 'form-postcode'}))

    address_line_1 = forms.CharField(
        label='address_line_1', max_length=150, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Address_Line_1', 'id': 'form-address1'}))


    address_line_2 = forms.CharField(
        label='address_line_2', max_length=150, widget=forms.TextInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'Address_Line_2', 'id': 'form-address2'}))


    class Meta:
        model = UserBase
        fields = ('email', 'user_name', 'first_name', 'phone_number')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user_name'].required = True
        self.fields['phone_number'].required = True
        self.fields['email'].required = True


class PwdResetForm(PasswordResetForm):
    email = forms.EmailField(max_length=250, widget=forms.TextInput(
        attrs={'class': 'form-control mb-3', 'placeholder': 'Email', 'id': 'form-email'}
    ))

    def clean_email(self):
        email = self.cleaned_data['email']
        user = UserBase.objects.filter(email=email)
        if not user:
            raise forms.ValidationError(
                _('There is no user with that email address')
            )
        return email


class PwdResetConfirmForm(SetPasswordForm):
    new_password1 = forms.CharField(
        label='New password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New password', 'id': 'form-newpass'}
        ))
    new_password2 = forms.CharField(
        label='Repeat password', widget=forms.PasswordInput(
            attrs={'class': 'form-control mb-3', 'placeholder': 'New password', 'id': 'form-new-pass2'}
        ))
