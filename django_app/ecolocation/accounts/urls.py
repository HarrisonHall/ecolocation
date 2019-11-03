# accounts/urls.py
from django.urls import path

from django.conf.urls.static import static
from . import views


urlpatterns = [
    path('signup/', views.SignUp.as_view(), name='signup'),
]
