# Generated by Django 4.2.14 on 2024-10-19 18:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('beta', '0004_feeddata_browsed_word'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='feeddata',
            name='browsed_word',
        ),
    ]
