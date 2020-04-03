from django.db import models
from django.utils.translation import gettext as _
# Create your models here.

class Brand(models.Model):
    BRDName = models.CharField(max_length=50, verbose_name=_('Brand Name'))
    BRDDesc = models.TextField(blank=True, null=True, verbose_name=_('Brand Description'))

    class Meta:
        verbose_name =_('Brand')
        verbose_name_plural =_('Brands')

    def __str__(self):
        return self.BRDName

class Varinant(models.Model):
    VARName = models.CharField(max_length=50, verbose_name=_('Varinant Name'))
    VARDesc = models.TextField(blank=True, null=True, verbose_name=_('Varinant Description'))

    class Meta:
        verbose_name =_('Varinant')
        verbose_name_plural =_('Varinants')

    def __str__(self):
        return self.VARName