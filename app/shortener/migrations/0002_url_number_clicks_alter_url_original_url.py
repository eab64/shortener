# Generated by Django 4.1.5 on 2023-02-03 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='number_clicks',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='url',
            name='original_url',
            field=models.TextField(unique=True),
        ),
    ]
