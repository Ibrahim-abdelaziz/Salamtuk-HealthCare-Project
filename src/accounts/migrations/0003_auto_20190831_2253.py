# Generated by Django 2.2.4 on 2019-08-31 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20190830_2259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='user',
            new_name='user_name',
        ),
    ]
