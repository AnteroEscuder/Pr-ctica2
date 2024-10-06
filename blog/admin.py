from django.contrib import admin

# Register your models here.

from .models import Coche
from .models import Propietario

admin.site.register(Coche)
admin.site.register(Propietario)