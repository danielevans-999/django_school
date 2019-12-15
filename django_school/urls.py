from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =  [
    
    path('',views.index,name='home'),
    path('accounts/student/', views.StudentSignup.as_view(), name='student'),
    path('accounts/teacher/', views.TeacherSignUpView.as_view(), name='teacher'),
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)