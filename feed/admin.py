from django.contrib import admin
from .models import Highlight

class HighlightAdmin(admin.ModelAdmin):
    pass

admin.site.register(Highlight, HighlightAdmin)
