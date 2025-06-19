from django.contrib import admin
from .models import Movie, Customer

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    fields = ['release_year', 'title', 'length']
    search_fields = ['title', 'release_year']
    list_filter = ['release_year']
    list_display = ['title', 'release_year', 'length']
    list_editable = ['length']

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    search_fields = ['first_name', 'last_name', 'phone']
    list_filter = ['last_name']
    list_display = ['first_name', 'last_name', 'phone']
    list_editable = ['phone']