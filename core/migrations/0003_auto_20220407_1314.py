# Generated by Django 3.1.1 on 2022-04-07 10:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20220407_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ll',
            name='name',
            field=models.CharField(max_length=64),
        ),
    ]
