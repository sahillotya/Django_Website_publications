# Generated by Django 3.0.5 on 2020-06-09 05:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('VRCpubs', '0005_auto_20200609_1029'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vrcpubs',
            name='publishedAt',
            field=models.DateField(),
        ),
    ]
