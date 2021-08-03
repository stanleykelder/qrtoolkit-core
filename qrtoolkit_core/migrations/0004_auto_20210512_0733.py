# Generated by Django 3.0.11 on 2021-05-12 07:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('qrtoolkit_core', '0003_department_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='departments', to=settings.AUTH_USER_MODEL),
        ),
    ]
