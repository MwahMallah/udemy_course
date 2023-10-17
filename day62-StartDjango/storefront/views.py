from django.http import HttpResponse


def name(request, name):
    return HttpResponse(f"Hello, {name}")