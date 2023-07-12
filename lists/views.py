from django.shortcuts import render
from django.http import HttpResponse


def view_index(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')