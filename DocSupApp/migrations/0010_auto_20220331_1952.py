# Generated by Django 3.0.6 on 2022-04-01 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocSupApp', '0009_auto_20220331_1949'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_fact_2',
            name='amount_ICA',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='detalle_fact_2',
            name='zSupplierName',
            field=models.CharField(max_length=100),
        ),
    ]
