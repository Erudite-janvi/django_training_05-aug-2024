# Generated by Django 5.0.7 on 2024-08-08 17:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sessionlogin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='last_name',
            field=models.CharField(default='unkonwn', max_length=200),
        ),
    ]
