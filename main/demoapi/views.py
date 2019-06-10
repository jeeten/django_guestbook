# Create your views here.
from django.shortcuts import render
from guest.models import User, Group
from rest_framework import viewsets
from main.demoapi.serealizers import UserSerailiser, GroupSerailiser

class UserViewSet(viewsets.ModelViewSet):
    """ 
    API endpoint that allows users to be viewed or edited.        
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer

class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serialiser_class = GroupSerailiser

    



