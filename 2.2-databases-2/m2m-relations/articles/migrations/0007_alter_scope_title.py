# Generated by Django 5.0.6 on 2024-06-07 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0006_alter_scope_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scope',
            name='title',
            field=models.CharField(default='почему-то это поле требовал джанго :D', max_length=256, verbose_name='Scope_title'),
        ),
    ]