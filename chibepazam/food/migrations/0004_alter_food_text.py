# Generated by Django 3.2.5 on 2021-08-24 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_alter_food_rate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='text',
            field=models.CharField(max_length=400),
        ),
    ]
