from django.urls import path, include
from testform import views

urlpatterns = [
    path('',views.contuct, name="Contuct"),
    path('guestlist/',views.guestList, name="guest_list"),
]
