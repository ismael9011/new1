from django.contrib import admin

# Register your models here.
from .models import Review
from .models import Properties
admin.site.register(Review)
admin.site.register(Properties)