from django.shortcuts import render
from django.http import HttpResponse


def view_index(request):
    '''Домашняя страница'''

    return render(request, 'lists/index.html', {
        'new_item_text': request.POST.get('item_text', '')
    })