from django.shortcuts import render,redirect
from django.views.generic import CreateView
from . models import User
from . forms import UserCreationForm

def index(request):
    return render(request, 'djangoschool/index.html')

class StudentSignup(CreateView):
    
    model = User
    form_class = UserCreationForm
    template_name = 'registration/signup_form.html'
    
    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'Student'
        return super().get_context_data(**kwargs)
    
    def form_valid(self, form):
        user = form.save()
        return redirect('home')