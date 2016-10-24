from django.shortcuts import render
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse("he he")


def shit(request):
    return HttpResponse("shit")


def af(request):
    return HttpResponse("aasaas")