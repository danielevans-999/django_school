from django.shortcuts import render,redirect
from django.views.generic import CreateView
from . models import *
from . forms import (StudentSignUpForm, TeachersSignUpForm, StudentProfileForm)
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def index(request):
    if request.user.is_authenticated:
        if request.user.user_type == 1:
            print('Hello teacher')
        else:
            return redirect('student_profile')
    return render(request, 'djangoschool/index.html')

class StudentSignup(CreateView):
    
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Student'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    
class TeacherSignUpView(CreateView):
    model = User
    form_class = TeachersSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Teacher'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')
    
def student_profile_info(request):
    
    current_user=request.user
    profile_info = StudentProfile.objects.filter(user=current_user).first()
    return render(request,'djangoschool/student-profile.html',{"profile":profile_info,"current_user":current_user})

def student_profile_edit(request):
    current_user = request.user
    if request.method == 'POST':
        form = StudentProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()
        return redirect('student_profile')

    else:
        form = StudentProfileForm()
        return render(request,'djangoschool/edit.html',{"form":form})
    
def update_profile(request):
    user_profile = StudentProfile.objects.get(user=request.user)
    
    if request.method == "POST":
        form =  StudentProfileForm(request.POST,request.FILES,instance=request.user.studentprofile)
        if form.is_valid():
            form.save()
        return redirect('home')
    else:
        form = StudentProfileForm(instance=request.user.studentprofile)
        return render(request,'djangoschool/update-profile.html',{"form":form})