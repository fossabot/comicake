# Generated by Django 2.0.2 on 2018-03-12 21:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reader', '0018_auto_20180312_1439'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='alt',
            field=models.CharField(blank=True, help_text='Name in native language', max_length=100),
        ),
    ]