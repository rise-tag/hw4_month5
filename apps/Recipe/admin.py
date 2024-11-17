
from django.contrib import admin
from apps.recipe.models import Recipe, Category

# Register your models here.

@admin.register(Recipe)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_active']
    list_filter = ['id', 'title', 'is_active']
    search_fields = ['id', 'title', 'is_active']
    list_editable = ['is_active', ]

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title']
