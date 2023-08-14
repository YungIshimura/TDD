from django.shortcuts import render, redirect
from .models import Item


def view_index(request):
    '''Домашняя страница'''
    items = Item.objects.all()
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])

        return redirect('/lists/my-list')

    return render(request, 'lists/index.html', {'items': items})


def view_list(request):
    '''Представление списка'''
    items = Item.objects.all()

    return render (request, 'lists/list.html', {'items': items})