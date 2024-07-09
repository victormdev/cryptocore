# Generated by Django 5.0 on 2024-02-20 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=500, unique=True)),
                ('userid', models.CharField(max_length=500, unique=True)),
                ('user_ans', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('video_file', models.FileField(upload_to='uploads/')),
                ('video_caption', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='Botinfo',
        ),
        migrations.RemoveField(
            model_name='message',
            name='group',
        ),
        migrations.DeleteModel(
            name='Groupinfo',
        ),
        migrations.DeleteModel(
            name='Message',
        ),
    ]