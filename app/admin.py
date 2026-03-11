from django.contrib import admin

from app.models import Service, Portfolio

# Register your models here.
admin.site.register(Portfolio)
admin.site.register(Service)