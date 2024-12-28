# book/admin.py
from django.contrib import admin
from .models import Service, FAQ, Blog

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'service_type', 'price_per_unit', 'availability', 'location') 
    list_filter = ('service_type', 'availability')  
    search_fields = ('name', 'description', 'location')  

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'answer')  
    search_fields = ('question',)  
    list_filter = ('question',)  

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'description')  
    search_fields = ('title', 'description')  
    list_filter = ('created_at',) 
    ordering = ('-created_at',)  
