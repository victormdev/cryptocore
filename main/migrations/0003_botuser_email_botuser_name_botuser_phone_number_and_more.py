# Generated by Django 5.0 on 2024-02-14 17:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_info'),
    ]

    operations = [
        migrations.AddField(
            model_name='botuser',
            name='email',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='botuser',
            name='name',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='botuser',
            name='phone_number',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='info',
            name='contact_us',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='membership',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='info',
            name='paymentmethod',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]