# Generated by Django 2.0.3 on 2018-03-18 13:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='author',
            old_name='carrier_start',
            new_name='was_born',
        ),
    ]