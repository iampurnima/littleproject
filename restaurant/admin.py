from django.contrib import admin
from .models import booking
from .models import menu

# Register your models here.
admin.site.register(booking)
admin.site.register(menu)