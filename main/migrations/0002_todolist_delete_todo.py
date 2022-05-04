# Generated by Django 4.0.2 on 2022-02-24 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ToDoList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('date', models.DateField()),
                ('checked', models.BooleanField(default=False)),
            ],
        ),
        migrations.DeleteModel(
            name='ToDo',
        ),
    ]
