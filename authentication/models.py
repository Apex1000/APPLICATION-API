from django.db import models
# Create your models here.
from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin)

from django.db import models
from rest_framework_simplejwt.tokens import RefreshToken

class UserManager(BaseUserManager):

    def create_user(self, username,first_name,last_name,phone_number,userrole, password=None):
        if username is None:
            raise TypeError('Users should have a username')

        user = self.model(username=username,first_name=first_name,last_name=last_name,userrole=userrole,phone_number=phone_number)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, username,first_name,last_name,phone_number,userrole,password=None):
        if password is None:
            raise TypeError('Password should not be none')

        user = self.create_user(username,first_name,last_name,phone_number,userrole, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

STATES = (
      ('UP', 'Worker'),
      ('MP', 'Secretary'),
      ('TP', 'Supervisor'),
      ('DP', 'Admin'),
    )
class Company(models.Model):
    username = models.CharField(max_length=150)
    company_name = models.CharField(max_length=150)
    company_phone_number = models.CharField(max_length=150,unique=True,)
    company_email = models.CharField(max_length=150,unique=True)
    address = models.CharField(max_length=150)
    state = models.CharField(choices=STATES,max_length=50)
    pincode = models.IntegerField()

    def __str__(self):
        return self.company_name

class Role(models.Model):
    """Role Detail model."""
    name = models.CharField(max_length=250, null=True, unique=True)

    def __str__(self):
        """__str__."""
        return str(self.name)

class User(AbstractBaseUser, PermissionsMixin):
    company = models.ForeignKey(Company,on_delete=models.SET_NULL,null=True,blank=True,related_name='company')
    first_name = models.CharField(max_length=70)
    last_name = models.CharField(max_length=70)
    phone_number = models.CharField(max_length=10)
    userrole = models.ForeignKey(Role,on_delete=models.SET_NULL,null=True,blank=True,related_name='userrole')
    username = models.CharField(max_length=255, unique=True, db_index=True)
    is_verified = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['first_name','last_name','phone_number','userrole']

    objects = UserManager()

    def __str__(self):
        return self.username

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }



class UserDetail(models.Model):
    STATES = (
      ('UP', 'Worker'),
      ('MP', 'Secretary'),
      ('TP', 'Supervisor'),
      ('DP', 'Admin'),
    )
    QUALIFICATIONS = (
      ('UP', 'Masters'),
      ('MP', 'Secretary'),
      ('TP', 'Supervisor'),
      ('DP', 'Admin'),
    )
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='user')
    address = models.CharField(max_length=150)
    state = models.CharField(choices=STATES,max_length=50)
    pincode = models.IntegerField()
    alternative_number = models.CharField(max_length=150,null=True)
    parents_name = models.CharField(max_length=50)
    parents_number = models.IntegerField()
    identification_id = models.CharField(max_length=50)
    qualification = models.CharField(choices=QUALIFICATIONS,max_length=20)

    def __str__(self):
        return self.user.username