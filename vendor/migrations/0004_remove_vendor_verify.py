# Generated by Django 3.2.8 on 2021-10-26 12:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vendor', '0003_auto_20211026_0114'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendor',
            name='verify',
        ),
    ]
