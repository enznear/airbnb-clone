# Generated by Django 3.2.6 on 2021-08-30 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='review',
            old_name='rooom',
            new_name='room',
        ),
    ]
