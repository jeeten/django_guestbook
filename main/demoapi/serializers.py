from guest.models import User, Group
from rest_framework import serializers

class UserSerializer(serializers.HyperLinkedModelSerializers):
    class Meta:
        model = User
        fields = ('url','username','email','group')

class GroupSerializer(serializers.HyperLinkedModelSerializers):
        class Meta:
            model = Group
            fields = ('url','name')
            

