# Generated by Django 4.1.4 on 2022-12-27 12:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fam', '0003_remove_familiar_fecha_de_nacimiento'),
    ]

    operations = [
        migrations.AddField(
            model_name='familiar',
            name='trabaja',
            field=models.BooleanField(default=True),
        ),
    ]
