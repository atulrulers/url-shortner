# Generated by Django 2.0.7 on 2018-07-22 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shortit', '0003_url_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='url',
            name='num_of_click',
            field=models.IntegerField(default=0),
        ),
    ]