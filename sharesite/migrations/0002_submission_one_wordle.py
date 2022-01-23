# Generated by Django 3.2 on 2022-01-23 00:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sharesite', '0001_initial'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='submission',
            constraint=models.UniqueConstraint(fields=('user', 'wordle'), name='one_wordle'),
        ),
    ]