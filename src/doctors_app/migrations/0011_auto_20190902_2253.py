# Generated by Django 2.2.4 on 2019-09-02 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors_app', '0010_auto_20190902_2251'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appoientment',
            name='appoientment_day',
            field=models.CharField(choices=[('saturday', 'saturday'), ('sunday', 'sunday'), ('monday', 'monday'), ('tuseday', 'tuseday'), ('wensday', 'wensday'), ('thursday', 'thursday'), ('friday', 'friday')], default='(select to)', max_length=250),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='Specialized',
            field=models.CharField(choices=[('Dermatologist', 'Dermatologist'), ('Neurologist', 'Neurologist'), ('Psychiatrist', 'Psychiatrist'), ('Bones', 'Bones'), ('Dentist', 'Dentist'), ('Cardiologist', 'Neurologist')], default='(select to)', max_length=50),
        ),
    ]
