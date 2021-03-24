from django.contrib import admin

# Register your models here.

#Register Todo Model
from .models import Todo
admin.site.register(Todo)

