# Generated by Django 2.0.3 on 2018-03-26 08:44

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0003_auto_20180326_0143'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='height',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default=django.utils.timezone.now, height_field='height', upload_to='', width_field='width'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='width',
            field=models.IntegerField(default=0),
        ),
    ]
