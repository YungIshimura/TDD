from django.contrib import admin
from django.urls import path
from lists.views import view_index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', view_index, name='index'),
]
