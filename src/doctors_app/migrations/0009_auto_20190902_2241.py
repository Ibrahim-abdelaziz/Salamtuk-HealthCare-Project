# Generated by Django 2.2.4 on 2019-09-02 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors_app', '0008_auto_20190902_2240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='Patient_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Booking', to='doctors_app.Paitent'),
        ),
        migrations.AlterField(
            model_name='booking',
            name='doctor_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='Booking', to='doctors_app.Doctor'),
        ),
    ]
