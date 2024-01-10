from django.contrib import admin
from .models import Category, Goods, Tag
from tinymce.widgets import TinyMCE
from django.db import models
import admin_thumbnails


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'activate', 'created', 'updated', 'url']
    list_filter = ['activate']
    search_fields = ['name', 'description']

    formfield_overrides = {
        models.TextField: {'widget': TinyMCE(attrs={'cols': 80, 'rows': 30})},
    }


@admin_thumbnails.thumbnail('image')
class GoodsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'activate', 'created', 'category']
    list_filter = ['activate', 'category']
    search_fields = ['name', 'description']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Goods, GoodsAdmin)
admin.site.register(Tag)
