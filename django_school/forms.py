from django import forms
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from . models import *


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'user_type', 'username',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserchangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'user_type',
                  'username', 'is_active', 'is_admin')

    def clean_password(self):
        return self.initial["password"]
    
    
class StudentSignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',  'username',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 2
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class TeachersSignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',  'username',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 1
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
class ParentSignUpForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email',  'username',)

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 3
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    
    
class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        exclude =['user']

class TeacherProfileForm(forms.ModelForm):
    class Meta:
        model = TeacherProfile
        exclude =['user']
        
class ResultUpdateForm(forms.ModelForm):
    class Meta:
        model = Result
        exclude = ['results', 'teacher']

class ParentProfileForm(forms.ModelForm):
    class Meta:
        model = ParentProfile
        exclude = ['user']