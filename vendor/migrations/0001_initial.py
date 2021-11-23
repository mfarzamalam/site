# Generated by Django 3.2.8 on 2021-10-24 08:08

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('file', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vendor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=50, verbose_name='Company name')),
                ('contact_name', models.CharField(max_length=50, verbose_name='Contact name')),
                ('address', models.CharField(max_length=150, verbose_name='Address')),
                ('zip_code', models.CharField(max_length=20, verbose_name='Zip Code')),
                ('verify', models.BooleanField(default=False, verbose_name='Verify')),
                ('file_1', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_1', to='file.file', verbose_name='File 1')),
                ('file_2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_2', to='file.file', verbose_name='File 2')),
                ('file_3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='file_3', to='file.file', verbose_name='File 3')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
            options={
                'verbose_name': 'vendor',
                'verbose_name_plural': 'vendors',
            },
        ),
    ]
