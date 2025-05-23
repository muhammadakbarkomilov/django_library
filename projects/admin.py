from django.contrib import admin
from projects.models import *

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'created')
    search_fields = ('title',)
    list_filter = ('created',)
    ordering = ('-created',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'created')
    search_fields = ('name',)
    list_filter = ('created',)
    ordering = ('-created',)
