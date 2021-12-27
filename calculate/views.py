from django.shortcuts import render
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from django.core import serializers
from django.conf import settings
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(["GET"])
def findfactorial(request):
    a=int(request.query_params.get('a'))
    factorial=1
    if a<0:
        return Response({"Print": "The factorial doesnt exist"})
    elif a==0:
        return Response({"Print": "The factorial of 0 is 1"})
    else:
        for i in range(1,a+1):
            factorial*=i
        return Response({"The factorial of {} is {} ".format(a,factorial)})


