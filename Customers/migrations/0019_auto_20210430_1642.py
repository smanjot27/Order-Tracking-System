# Generated by Django 3.1.7 on 2021-04-30 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0018_orderupdt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderupdt',
            name='order_id',
            field=models.IntegerField(),
        ),
    ]