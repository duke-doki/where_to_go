# Generated by Django 4.2.8 on 2024-01-08 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0015_alter_image_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.IntegerField(blank=True, db_index=True, default=0, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='place',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Место'),
        ),
    ]
