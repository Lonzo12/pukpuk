from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Numbers)
admin.site.register(Products)
class NumbersAdmin(admin.ModelAdmin):
    list_display = ('nomer','date_bron','date_zaezda','date_viezda','status')

admin.site.register(Profile)
