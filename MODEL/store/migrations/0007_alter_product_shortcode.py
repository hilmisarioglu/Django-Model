# Generated by Django 3.2.9 on 2021-12-05 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0006_alter_product_shortcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='shortcode',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
