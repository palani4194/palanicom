# Generated by Django 2.0 on 2018-04-25 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='emp_id',
            field=models.IntegerField(),
        ),
    ]
