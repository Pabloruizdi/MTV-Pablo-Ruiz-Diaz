# Generated by Django 4.1.4 on 2022-12-27 12:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fam', '0004_familiar_trabaja'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='trabaja',
            field=models.BooleanField(default=False),
        ),
    ]
