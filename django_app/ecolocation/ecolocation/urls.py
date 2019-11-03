"""ecolocation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
#from . import views
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic.base import TemplateView # new
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('make_event/', views.make_event),

    path('test/', views.Test),
    #path('make_event', TemplateView.as_view(template_name='events/make_event.html'), name='make_event')
    path('make_event', views.create_event, name='make_event'),
    
    path('view_tags', views.view_tags, name='view_tags'),
    path('view_tags_single', views.view_tags_single, name='view_tags_single'),
    
    path('check_event', TemplateView.as_view(template_name='events/check_event.html'), name="check_event"),
    path('check_event/', views.check_event2, name="check_event2"),
]
