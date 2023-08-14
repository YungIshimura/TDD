from django.contrib import admin
from django.urls import path
from lists.views import view_index, view_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_index, name='index'),
    path('lists/my-list/', view_list, name='list')
]
