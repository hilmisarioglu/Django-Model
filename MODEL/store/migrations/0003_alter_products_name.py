# Generated by Django 3.2.9 on 2021-12-05 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20211205_1142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='name',
            field=models.CharField(blank=True, default='Ürün ...', max_length=50, null=True),
        ),
    ]
