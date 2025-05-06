from django.contrib import admin
from apps.contact.models import Contacts


class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name', 'email', 'subject', 'message', 'update_at', 'created_at']

admin.site.register(Contacts, ContactAdmin)

