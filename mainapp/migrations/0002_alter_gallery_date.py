# Generated by Django 3.2.9 on 2022-03-05 15:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='date',
            field=models.DateTimeField(),
        ),
    ]
