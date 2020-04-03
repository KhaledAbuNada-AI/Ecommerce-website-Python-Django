from django.contrib import admin

# Register your models here.

from .models import Product
from .models import ProductImage
from .models import Category
from .models import Product_Alternatives
from .models import Product_Accessoris


admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
admin.site.register(Product_Alternatives)
admin.site.register(Product_Accessoris)