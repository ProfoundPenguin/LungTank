# Generated by Django 4.2.15 on 2024-10-02 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_alter_review_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='sales_count',
            field=models.PositiveIntegerField(default=224),
        ),
    ]
