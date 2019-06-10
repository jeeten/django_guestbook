"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples: 
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth.models import User
from guest.models import User
# from rest_framework import routers, serializers, viewsets
from rest_framework import routers, serializers, viewsets
# from .views import classroom, students, teachers
# from . import views
# from main.guest.views import views

# form .views import
from guest.views import SignUpView, StudentSignUpView, ProfileHomeView
from guest import views
# from guest.admin import user_admin_site
# signup
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register('users', UserViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup/', views.signup, name='signup'),
    path('accounts/signup/student/', StudentSignUpView.as_view(), name='user_signup'),
    path('accounts/home/', ProfileHomeView.as_view(), name='home'),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls',namespace='rest_framework')),
    # path('', include(user_admin_site.urls)),
    # path('accounts/signup/teacher/', teachers.TeacherSignUpView.as_view(), name='teacher_signup'),
]
