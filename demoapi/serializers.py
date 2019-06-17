from guest.models import User,Guest
from django.contrib.auth.models import Group
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','username','email','is_staff')

class GroupSerializer(serializers.HyperlinkedModelSerializer):
        class Meta:
            model = Group
            fields = ('url','name')
class GuestSerializer(serializers.ModelSerializer):
        class Meta:
            # db_table = ''
            # managed = True
            # model = Guest
            # fields = ('des')
            model = Guest
            fields = ('id','descriptin','image')
                
            def __str__(self):
                pass
                

