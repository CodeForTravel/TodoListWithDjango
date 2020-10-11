from django.urls import path
from . import views

urlpatterns = [
    path('profile/<username>/',views.Profile, name='profile'),

]