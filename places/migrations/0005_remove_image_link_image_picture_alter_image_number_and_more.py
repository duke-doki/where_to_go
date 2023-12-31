# Generated by Django 4.2.8 on 2023-12-26 07:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0004_image_number'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='link',
        ),
        migrations.AddField(
            model_name='image',
            name='picture',
            field=models.ImageField(blank=True, upload_to='', verbose_name='Картинка'),
        ),
        migrations.AlterField(
            model_name='image',
            name='number',
            field=models.IntegerField(blank=True, null=True, verbose_name='Номер'),
        ),
        migrations.AlterField(
            model_name='image',
            name='place',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='images', to='places.place', verbose_name='Связь с местом'),
        ),
    ]
