# Generated by Django 3.1.5 on 2021-01-22 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20210122_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='small_image',
            field=models.URLField(null=True),
        ),
    ]
