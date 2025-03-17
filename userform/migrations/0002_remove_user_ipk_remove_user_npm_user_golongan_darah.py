# Generated by Django 5.1 on 2025-03-17 06:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userform', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='ipk',
        ),
        migrations.RemoveField(
            model_name='user',
            name='npm',
        ),
        migrations.AddField(
            model_name='user',
            name='golongan_darah',
            field=models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('O+', 'O+'), ('O-', 'O-'), ('AB+', 'AB+'), ('AB-', 'AB-')], default=0, help_text='Pilih golongan darah dari predefined value', max_length=3),
            preserve_default=False,
        ),
    ]
