from django.db import models
from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser)


class MyUserManager(BaseUserManager):
    
    def create_user(self, email, user_type,username, password=None):
        
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            
            email=self.normalize_email(email),
            username = username,
            user_type = user_type,
        )
        
        user.set_password(password)
        user.save(using = self._db)
        return user
    
    def create_superuser(self, email, user_type, username, password=None):
        
        user = self.create_user(
            
            email,
            user_type = user_type,
            username = username,
            password=password,
            
        )
        
        user.is_admin = True
        user.save(using = self._db)
        return user

class User(AbstractBaseUser):
    
    USER_TYPE_CHOICES = (
        
        (1, 'Teacher'),
        (2, 'Student'),
        (3, 'Parent'),
    )
    
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, unique=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    
    USERNAME_FEILD = 'email'
    REQUIRED_FIELDS = ['username', 'user_type', ]
    
    objects = MyUserManager()
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):
        return True
    
    def has_module_perms(self, app_label):
        return True
    
    @property
    def is_staff(self):
        return self.is_admin


