# Generated by Django 2.2.1 on 2019-07-11 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0011_courseusers'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courselist',
            name='date_begin',
            field=models.DateTimeField(default='1970-01-01'),
        ),
    ]
