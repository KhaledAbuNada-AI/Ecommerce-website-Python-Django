# Generated by Django 3.0.3 on 2020-03-24 19:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20200324_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='CATParent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Category', verbose_name='SubCategory'),
        ),
    ]
