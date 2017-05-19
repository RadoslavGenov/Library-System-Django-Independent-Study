from django.contrib.auth.models import User
from django.forms import ModelForm, ValidationError
from django import forms
from .models import Books


class BooksForm(ModelForm):
    class Meta:
        model = Books
        fields = ('picture', 'name', 'publisher', 'author')

    def clean_name(self):
        name = self.cleaned_data['name']
        if Books.objects.filter(name=name).exists():
            raise ValidationError("A Book with that name already exists!")
        return name


class SearchForm(forms.Form):
    book_name = forms.CharField(max_length=100)


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)


class MemberRegistration(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat Password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Password don\'t match')
        return cd['password2']

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists!")
        return email