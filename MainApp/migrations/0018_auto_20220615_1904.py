# Generated by Django 3.2.10 on 2022-06-15 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MainApp', '0017_school1'),
    ]

    operations = [
        migrations.DeleteModel(
            name='School1',
        ),
        migrations.AddField(
            model_name='school',
            name='teachers',
            field=models.JSONField(default='0'),
        ),
    ]
