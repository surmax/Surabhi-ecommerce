# Generated by Django 4.0.4 on 2023-02-28 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='product',
            name='thumbnail',
            field=models.CharField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]