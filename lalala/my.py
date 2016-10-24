from django.http import HttpResponse
from django.shortcuts import render


def my(request):
    return HttpResponse("mm")
