# Generated by Django 4.2.11 on 2024-06-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='tour_destinations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('destination_img', models.ImageField(upload_to='destination_img/')),
                ('district', models.CharField(max_length=300)),
                ('state', models.CharField(max_length=300)),
                ('map_link', models.URLField()),
                ('weather', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=900)),
            ],
        ),
    ]
