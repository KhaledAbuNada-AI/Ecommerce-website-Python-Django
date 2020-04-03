from django.db import models
from django.contrib import admin
from django.utils.translation import gettext as _
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.


class Product(models.Model):
    PRODName = models.CharField(max_length=100, verbose_name=_("Product Name"))
    PRODCategory = models.ForeignKey('Category', on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('Product Category'))
    PRODBrand = models.ForeignKey('setting.Brand', on_delete= models.CASCADE, blank=True, null=True, verbose_name=_('Product Brand'))
    PRODDesc = models.TextField(verbose_name=_("Product Description"))
    PRODImage = models.ImageField(upload_to='prodcut/', verbose_name=_('Image'), blank=True, null=True)
    PRODPrice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Price"))
    PRODDiscountPrice = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Discount Price"))
    PRODCost = models.DecimalField(max_digits=5, decimal_places=2, verbose_name=_("Cost"))
    PRODCreated = models.DateTimeField(verbose_name=_("Created At"))
    PRODSLug = models.SlugField(blank=True, null=True, verbose_name=_("Product URL"))
    PRODISNew = models.BooleanField(default=True, verbose_name=_("New Product"))
    PRODISBestSeller = models.BooleanField(default=False, verbose_name=_("Best Seller"))

    def save(self, *args, **kwargs):
        if not self.PRODSLug:
            self.PRODSLug = slugify(self.PRODName)
        super(Product, self).save(*args, **kwargs)

    class Meta:
        verbose_name =_("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        return reverse('product:product_detail',kwargs={'slug': self.PRODSLug})


    def __str__(self):
       return self.PRODName


class ProductImage(models.Model):
    PRDIProduct = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name=_("Product"))
    PRDIImage = models.ImageField(upload_to='product/', verbose_name=_("Image"))

    def __str__(self):
        return str(self.PRDIProduct)

class Category(models.Model):
    CATName = models.CharField(max_length=50, verbose_name=_('Name'))
    CATParent = models.ForeignKey('self', limit_choices_to={'CATName__isnull': True}, on_delete=models.CASCADE, blank=True, null=True, verbose_name=_('Main Category'))
    CATDesc = models.TextField(verbose_name=_('Description'))
    CATImg = models.ImageField(upload_to='category/', verbose_name=_('Image'))

    class Meta:
        verbose_name =_("Category")
        verbose_name_plural =_("Categorys")

    def __str__(self):
        return self.CATName


class Product_Alternatives(models.Model):
    PALNProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='main_product',verbose_name=_('Product'))
    PALNAlternatives = models.ManyToManyField(Product, related_name='alternatives_products', verbose_name=_('Alternatives'))


    class Meta:
        verbose_name =_("Product Alternative")
        verbose_name_plural =_("Product Alternatives")

    def __str__(self):
        return str(self.PALNProduct)


class Product_Accessoris(models.Model):
    PACCProduct = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='mainAccessory_product', verbose_name=_('Product'))
    PACCAlternatives = models.ManyToManyField(Product, related_name='accessories_products', verbose_name=_('Accessories'))


    class Meta:
        verbose_name =_("Product Accessory")
        verbose_name_plural =_("Product Accessories")

    def __str__(self):
        return str(self.PACCProduct)





## Category
## Img ##
## Alternatives
## Accessoris
## Translation
## Verbose names
## get absl url
## product tags
## pagination
## Url Slug