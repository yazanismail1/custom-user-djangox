# Generated by Django 4.1.1 on 2022-12-06 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('countries', '0002_remove_country_country_qoute_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='country',
            name='continent',
            field=models.CharField(default='', max_length=56),
        ),
    ]
