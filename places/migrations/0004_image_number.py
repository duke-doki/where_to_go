# Generated by Django 4.2.8 on 2023-12-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0003_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='номер'),
        ),
    ]
