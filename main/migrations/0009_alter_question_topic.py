# Generated by Django 5.0 on 2024-03-12 20:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_question_topic_delete_tripdetail_delete_video_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questions', to='main.topic'),
        ),
    ]
