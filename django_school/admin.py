from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . models import User
from . forms import *

class UserAdmin(BaseUserAdmin):
    form = UserchangeForm
    add_form = UserCreationForm
    
    list_display = ('email', 'user_type','username', 'is_admin')
    list_filter = ('is_admin', )
    
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('user_type',)}),
        ('Permissions', {'fields': ('is_admin',)}),
    )
    
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'user_type','username', 'password1', 'password2'),
        }),
    )
    
    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()
    
admin.site.register(User, UserAdmin)

admin.site.unregister(Group)


