# Generated by Django 2.2.3 on 2019-07-21 10:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='year_of_birth',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
