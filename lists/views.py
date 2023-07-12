from django.shortcuts import render
from django.http import HttpResponse


def view_index(request):
    return render(request, 'lists/index.html')