# Generated by Django 4.0.3 on 2022-04-26 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='beginning_of_movie',
            field=models.DateField(blank=True, null=True),
        ),
    ]
