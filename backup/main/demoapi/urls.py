from django.urls import path, include
from rest_framework import routers
from demoapi import views


router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('rest-auth/', include('rest_auth.urls')),
    path('guest/', views.ListGuest.as_view()),
    path('guest/<int:pk>/', views.DetailGuest.as_view())
]