# Generated by Django 2.2.4 on 2019-09-02 20:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors_app', '0006_auto_20190902_0947'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comments',
            name='user',
        ),
        migrations.AddField(
            model_name='comments',
            name='Paitent',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Paitents', to='doctors_app.Paitent'),
        ),
    ]
