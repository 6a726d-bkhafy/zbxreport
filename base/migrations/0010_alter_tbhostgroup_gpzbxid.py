# Generated by Django 5.0.3 on 2024-03-25 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_tbapi_apitoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbhostgroup',
            name='gpzbxid',
            field=models.IntegerField(unique=True),
        ),
    ]
