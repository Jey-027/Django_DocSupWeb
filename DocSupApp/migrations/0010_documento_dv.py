# Generated by Django 3.0.6 on 2022-07-07 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocSupApp', '0009_auto_20220418_0951'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='dv',
            field=models.IntegerField(null=True),
        ),
    ]
