from django.db import models


from django.db import models


class List(models.Model):
    '''список'''
    pass

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, null=True, default=None, on_delete=models.PROTECT)