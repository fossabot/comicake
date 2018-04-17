# Generated by Django 2.0.2 on 2018-03-12 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0019_auto_20180312_1440'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tag',
            name='stub',
        ),
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(default='lol', max_length=20, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tag',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]