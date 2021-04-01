# Generated by Django 3.0.2 on 2021-03-31 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Calorie', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userfooditem',
            name='customer',
        ),
        migrations.AddField(
            model_name='userfooditem',
            name='customer',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='Calorie.Customer'),
        ),
    ]
