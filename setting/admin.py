from django.contrib import admin

# Register your models here.
from .models import Brand
from .models import Varinant

admin.site.register(Brand)
admin.site.register(Varinant)
