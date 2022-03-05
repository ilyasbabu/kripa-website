from django.contrib import admin
from . models import Gallery

# Register your models here.
class GalleryAdmin(admin.ModelAdmin):
    list_display = ('title','date')
    list_display_links = ('title','date')
    list_filter = ('title','image','date')
    # list_editable = ('title','image','date')
    search_fields = ('title','image','date')
admin.site.register(Gallery,GalleryAdmin)
