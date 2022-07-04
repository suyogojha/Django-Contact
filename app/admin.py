from django.contrib import admin

# Register your models here.
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'gender', 'info', 'phone')
    list_display_names = ('id', 'name')
    list_editable = ('info',)
    list_filter = ('gender', 'date_added')
    list_per_page = 10


admin.site.register(Contact, ContactAdmin)
