from django.contrib import admin
from projects.models import Project, Category
from django.conf import settings

class ProjectAdmin(admin.ModelAdmin):
    pass

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Project, ProjectAdmin)
admin.site.register(Category, CategoryAdmin)
