# Generated by Django 4.1 on 2022-08-23 14:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='titles',
            new_name='title',
        ),
    ]