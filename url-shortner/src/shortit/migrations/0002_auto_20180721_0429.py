# Generated by Django 2.0.7 on 2018-07-20 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortit', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='shortcode',
            field=models.CharField(blank=True, max_length=15, unique=True),
        ),
    ]
