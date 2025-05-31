from django.contrib import admin

from customers.models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ['name', 'cpf', 'phone', 'create_at']
    search_fields = ['name', 'cpf', 'phone']



# Register your models here.
