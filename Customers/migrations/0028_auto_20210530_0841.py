# Generated by Django 3.1.7 on 2021-05-30 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0027_auto_20210530_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='process',
            name='cylsize',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]