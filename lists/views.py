from django.shortcuts import render, redirect
from .models import Item


def view_index(request):
    '''Домашняя страница'''
    items = Item.objects.all()
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        print(request.POST)
        return redirect('/')

    return render(request, 'lists/index.html', {'items': items})
