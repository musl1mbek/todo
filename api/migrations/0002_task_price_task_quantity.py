# Generated by Django 4.0.3 on 2022-03-23 05:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='price',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='quantity',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]
