# Generated by Django 3.1.5 on 2021-01-22 12:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0003_remove_item_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='metall',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='proba',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='size',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='style',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='vstavka',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='item',
            name='weight',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
