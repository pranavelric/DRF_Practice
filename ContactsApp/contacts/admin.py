from django.contrib import admin
from .models import Contact
# Register your models here.
@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['id', 'owner', 'country_code', 'first_name', 'last_name', 'phone_number', 'contact_pic',
                  'is_favourite']
