# Generated by Django 5.1.1 on 2024-09-25 12:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='instructor',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='present',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='feechallan',
            name='paid',
            field=models.BooleanField(default=False),
        ),
    ]
