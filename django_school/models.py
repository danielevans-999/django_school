from django.db import models
from django.contrib.auth.base_user import (BaseUserManager, AbstractBaseUser)



class MyUserManager(BaseUserManager):

    def create_user(self, email, user_type, username, password=None):

        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(

            email=self.normalize_email(email),
            username=username,
            user_type=user_type,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, user_type, username, password=None):

        user = self.create_user(

            email,
            user_type=user_type,
            username=username,
            password=password,

        )

        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):

    USER_TYPE_CHOICES = (

        (1, 'Teacher'),
        (2, 'Student'),
        (3, 'Parent'),
    )

    email = models.EmailField(max_length=100, unique=True)
    username = models.CharField(max_length=100)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'user_type']

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


class StudentProfile(models.Model):
    grade_level_choices = (
        (1, 'Grade_one'),
        (2, 'Grade_two'),
        (3, 'Grade_three'),
        (4, 'Grade_four'),
        (5, 'Grade_five'),
        (6, 'Grade_six'),
        (7, 'Grade_seven'),
        (8, 'Grade_eight'),
    )
    admission_no = models.CharField(max_length=100, unique=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    phone = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='pictures/')
    grade = models.IntegerField(choices=grade_level_choices, null=True, blank=True)
    user = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE)



class Result(models.Model):

    term_1 = models.CharField(max_length=5)
    term_2 = models.CharField(max_length=5)
    tem_3 = models.CharField(max_length=5)
    results = models.OneToOneField(
        StudentProfile, primary_key=True, on_delete=models.CASCADE)
    teacher = models.ForeignKey('TeacherProfile', on_delete=models.CASCADE)


class TeacherProfile(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    photo = models.ImageField(upload_to='photo/')
    phone = models.IntegerField(blank=True, null=True)
    user = models.OneToOneField(
        User, primary_key=True, on_delete=models.CASCADE)





