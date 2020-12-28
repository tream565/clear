from django.conf.urls import include, url
from django.urls import path
from login import views

urlpatterns = [
    url(r'^login/',views.sign_in),
    url(r'^ok/',views.ok),
    url(r'^logout/',views.log_out),
]