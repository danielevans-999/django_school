from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =  [
    
    path('',views.index,name='home'),
    path('accounts/student/', views.StudentSignup.as_view(), name='student'),
    path('accounts/teacher/', views.TeacherSignUpView.as_view(), name='teacher'),
    path ('accounts/student/profile/', views.student_profile_info, name='student_profile'),
    path ('accounts/student/edit/', views.student_profile_edit, name='stdedit_profile'),
    path ('accounts/student/update/', views.update_profile, name='update_profile'),
    path ('accounts/teacher/profile/', views.teacher_profile_info, name='teacher_profile')
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)