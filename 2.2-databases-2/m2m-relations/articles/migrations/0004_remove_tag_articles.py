# Generated by Django 5.0.6 on 2024-06-07 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_remove_scope_quantity_scope_is_main_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='articles',
        ),
    ]