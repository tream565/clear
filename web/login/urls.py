from django.conf.urls import include, url
from django.urls import path
from login import views

urlpatterns = [
    url(r'^log/',views.sign_in),
    url(r'^ok/',views.ok),
]