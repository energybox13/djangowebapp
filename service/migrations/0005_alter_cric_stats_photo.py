# Generated by Django 5.0 on 2023-12-30 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('service', '0004_alter_cric_stats_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cric_stats',
            name='photo',
            field=models.ImageField(default='test1/media_main/defaut.jpg', upload_to='test1/media_main/'),
        ),
    ]
