# Generated by Django 5.0 on 2023-12-30 09:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0002_cric_stats_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cric_stats',
            name='photo',
            field=models.ImageField(default='/service/media/', upload_to='media/'),
        ),
    ]
