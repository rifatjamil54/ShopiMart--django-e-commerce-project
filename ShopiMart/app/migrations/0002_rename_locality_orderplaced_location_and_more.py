# Generated by Django 4.1.7 on 2023-04-24 17:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderplaced',
            old_name='locality',
            new_name='location',
        ),
        migrations.RenameField(
            model_name='orderplaced',
            old_name='city',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='orderplaced',
            old_name='zipcode',
            new_name='phone_number',
        ),
    ]
