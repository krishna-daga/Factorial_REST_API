from django.urls import path
from rest_framework import routers, serializers, viewsets
from django.conf.urls import url
from . import views

urlpatterns = [
    path("findfactorial/",views.findfactorial, name="findfactorial")

]