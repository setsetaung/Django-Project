# Generated by Django 3.0.2 on 2021-03-31 01:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Calorie', '0002_auto_20210331_1027'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfooditem',
            name='customer',
        ),
        migrations.AddField(
            model_name='userfooditem',
            name='customer',
            field=models.ManyToManyField(blank=True, to='Calorie.Customer'),
        ),
    ]
