# Generated by Django 3.2.9 on 2021-12-19 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('request_quote', '0002_remove_item_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='requirementsdoc',
            name='updated_at',
        ),
        migrations.AddField(
            model_name='quote',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='quote',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]