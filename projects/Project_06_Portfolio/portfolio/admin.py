from django.contrib import admin
from .models import Category as CategoryModel, Entry

# Register your models here.
admin.site.register(CategoryModel)
admin.site.register(Entry)