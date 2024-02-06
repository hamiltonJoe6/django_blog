from django.contrib import admin
from . import models

@admin.register(models.Blog)
class BlogAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('title',), }

admin.site.register(models.Category)
