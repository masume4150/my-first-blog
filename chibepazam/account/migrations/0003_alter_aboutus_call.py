# Generated by Django 3.2.5 on 2021-09-01 07:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_aboutus_idea'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutus',
            name='call',
            field=models.CharField(max_length=11, verbose_name='شماره تماس'),
        ),
    ]
