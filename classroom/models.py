from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from .managers import MyUserManager



class User(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )

    is_active = models.BooleanField(default=True)
    #is_student = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    #is_teacher = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


class Problem(models.Model):
    name = models.CharField(max_length=30,default="problem1")
    #grade=models.IntegerField(blank=True, null=True)
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.name



class Student(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    id_num=models.IntegerField(default=0)


    def __str__(self):
        return str(self.id_num)

class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    #id_num=models.IntegerField()
    def __str__(self):
        return self.user.username
class ProblemAnswer(models.Model):
    student=models.ForeignKey(Student,on_delete=models.CASCADE,blank=True, null=True)
    senttime=models.DateTimeField(auto_now_add=True)
    document = models.FileField(upload_to='documents/',blank=True)
    problem=models.ForeignKey(Problem,on_delete=models.CASCADE,blank=True, null=True)
    grade=models.IntegerField(blank=True, null=True)
    def __str__(self):

        return str (self.student)

class Videos(models.Model):
    title = models.CharField(max_length=100)
    video = models.FileField(upload_to='videos/')

    def __str__(self):
        return self.title
