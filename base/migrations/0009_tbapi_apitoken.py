# Generated by Django 5.0.3 on 2024-03-24 17:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0008_alter_tbapi_apipass'),
    ]

    operations = [
        migrations.AddField(
            model_name='tbapi',
            name='apitoken',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
