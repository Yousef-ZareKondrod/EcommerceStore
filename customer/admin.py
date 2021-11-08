from django.contrib import admin

# Register your models here.
from customer.models import UserBase

admin.site.register(UserBase)
