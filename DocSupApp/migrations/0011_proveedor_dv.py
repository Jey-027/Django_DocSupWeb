# Generated by Django 3.0.6 on 2022-07-08 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocSupApp', '0010_documento_dv'),
    ]

    operations = [
        migrations.AddField(
            model_name='proveedor',
            name='dv',
            field=models.IntegerField(null=True),
        ),
    ]
