# Generated by Django 3.2.9 on 2021-12-07 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dj_relationships', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Boolean',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('boolean', models.BooleanField()),
            ],
        ),
    ]
