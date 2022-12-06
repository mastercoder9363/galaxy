from django.contrib import admin

# Register your models here.
from .models import *



@admin.register(Moshina)
class ArticleMoshina(admin.ModelAdmin):
    list_filter = ('name',)
    list_display = ('name', 'tanlov')