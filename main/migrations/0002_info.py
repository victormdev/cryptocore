# Generated by Django 5.0 on 2024-02-12 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('welcome_text', models.TextField()),
                ('rules', models.TextField()),
                ('agree_text', models.TextField()),
            ],
        ),
    ]