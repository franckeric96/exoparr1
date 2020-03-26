from django.contrib import admin

from . import models

from django.utils.safestring import mark_safe

from actions import Actions

# Register your models here.
class ServiceAdmin(Actions):
    fieldsets = [
        ('Presentation',{'fields': ['nom','image']}),
        ('Standard', {'fields': ['description','status']})
        
    ]
    
    
    list_display = ('nom','date_add','status','image_views')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    
     def image_views(self,obj):
        return mark_safe("<img src='{url}' width= 100px height=50px >".format(url=obj.image.url))

    
class SeasonAdmin(Actions):
    
    fieldsets = [
        ('Presentation',{'fields': ['image','nom','description']}),
        ('Status',{'fields': ['status']})
    ]
    
    list_display = ('nom','date_add','status','image_views')
    list_filter = ('status',)
    search_fields = ('nom',)
    date_hierarchy = "date_add"
    list_display_links = ['nom']
    ordering = ['nom']
    list_per_page = 10
    
    def image_views(self,obj):
        return mark_safe("<img src='{url}' width= 100px height=50px >".format(url=obj.image.url))

class GallerieAdmin(Actions):
    
    fieldsets = [
        ('Presentation',{'fields': ['image','titre']}),
        ('Status',{'fields': ['status']})
       
    ]
    
    list_display = ('titre','date_add','status','image_views')
    list_filter = ('status',)
    search_fields = ('titre',)
    date_hierarchy = "date_add"
    list_display_links = ['titre']
    ordering = ['titre']
    list_per_page = 10
    
    def image_views(self,obj):
        return mark_safe("<img src='{url}' width= 100px height=50px >".format(url=obj.image.url))

                                                                                                                                  
    
    


    
def _register(model,Admin_class):
    admin.site.register(model,Admin_class)

_register(models.Service, ServiceAdmin)  
_register(models.Gallerie, GallerieAdmin) 
_register(models.Season, SeasonAdmin) 

 