# Generated by Django 3.0.6 on 2022-04-01 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DocSupApp', '0007_detalle_fact_2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='detalle_fact_2',
            name='name_supplier',
            field=models.CharField(max_length=100),
        ),
    ]