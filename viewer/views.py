from django.http import HttpResponse
from django.shortcuts import render


def hello(request):
    # zde by byla funkcionalita
    return HttpResponse("Hello, world!")


def hello2(request, s):
    # zde by byla funkcionalita
    return HttpResponse(f"Hello, {s} world!")


def hello3(request):
    s = request.GET.get("s", "")
    return HttpResponse(f"Hello, {s} world!")


def hello4(request, s):
    t = request.GET.get("t", "")
    return HttpResponse(f"Your words: {s}, {t}")


def add(request, num1, num2):
    return HttpResponse(f"Adding {num1} + {num2} = {num1 + num2}")


def add2(request):
    num1 = int(request.GET.get("num1", 0))
    num2 = int(request.GET.get("num2", 0))
    return HttpResponse(f"Adding {num1} + {num2} = {num1 + num2}")





