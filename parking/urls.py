"""parking URL Configuration

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
from django.urls import path
from django.conf.urls import url

from reservation import views as core_views

from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from reservation.views import ReservationView, ReservationsListView

# kjsfkdjs

urlpatterns = [
    # url(r'^$', TemplateView.as_view(template_name='registration/home.html'), name='home'),
    url(r'^$', core_views.signup, name='signup'),
    url(r'^login/$',auth_views.LoginView.as_view(template_name="registration/login.html"), name="login"),
    url(r'^logout/$',auth_views.LogoutView.as_view(template_name="registration/logged_out.html"), name="logout"),
    url(r'^admin/', admin.site.urls),
    url(r'^reservationList/', ReservationsListView.as_view(), name='reservations_list'),
    url(r'^reservation/', ReservationView.as_view(), name='index'),
]
