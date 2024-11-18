from django.contrib import admin

from sacco.models import Deposit, Customer

# Register your models here.
admin.site.site_header = 'Umoja Sacco Administration'
admin.site.site_title = 'Sacco Admin'

class CustomerAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'gender']
    search_fields = ['first_name', 'last_name', 'email']
    list_filter = ['gender']
    list_per_page = 25

class DepositAdmin(admin.ModelAdmin):
    list_display = ['customer', 'created_at', 'status', 'amount']
    search_fields = ['customer', 'status', 'amount']
    list_per_page = 25
    list_filter = ['status']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Deposit, DepositAdmin)





# python3 manage.py --help
# python3 manage.py createsuperuser

# admin@gmail.com ---username & email
# 123456 ---password
# Hrp@Ssword

# localhost:8006/admin