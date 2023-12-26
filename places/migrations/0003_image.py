# Generated by Django 4.2.8 on 2023-12-24 11:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0002_auto_20231224_1325'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link', models.ImageField(blank=True, upload_to='', verbose_name='Ссылка на картинку')),
                ('place', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='places.place', verbose_name='Связь с местом')),
            ],
        ),
    ]
