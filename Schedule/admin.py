from django.contrib import admin
from .models import Data, Data

class ListandoServicos(admin.ModelAdmin):
    list_display = ('id', 'categoria')

admin.site.register(Data, ListandoServicos)