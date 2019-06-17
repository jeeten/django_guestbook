from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.html import escape, mark_safe

# from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

# Create your models here.

class User(AbstractUser):
    is_guest = models.BooleanField(default=False)
    is_approver = models.BooleanField(default=False)
    
    
# class GuestUser():

class Guest(models.Model):
    # id = models.AutoField(max_length=20,unique=True,primary_key=True)
    descriptin = models.TextField(max_length=200,editable=True,null=True)
    image = models.ImageField(upload_to = "profile/",default="no_image.jpg",verbose_name="Profile Pic")
    author = models.ForeignKey(User,to_field='id',on_delete=models.DO_NOTHING)
    # author = models.OneToOneField(User, on_delete=models.CASCADE,unique=True)
    addeddate = models.DateField(auto_now=True)
    updateddate = models.DateField(auto_now=True)

    def __str__(self):
        return self.descriptin

    def get_string_fields(self):
        # list of some excluded fields
        excluded_fields = ['id']

        # getting all fields that available in `Client` model,
        # but not in `excluded_fields`
        field_names = [field.name for field in Guest._meta.get_fields() 
                       if field.name not in excluded_fields]
        values = []
        for field_name in field_names:
            # get specific value from instanced object.
            # and outputing as `string` value.
            values.append('%s' % getattr(self, field_name))

        # joining all string values.
        return ' | '.join(values)        

    # class Meta:
    #     # table_name = "guest"
    #     db_table = 'Guest'


    
