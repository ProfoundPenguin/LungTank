# Generated by Django 4.2.15 on 2024-09-29 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('view', '0003_landing'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landing',
            name='video',
            field=models.FileField(upload_to='landing_video/'),
        ),
    ]
