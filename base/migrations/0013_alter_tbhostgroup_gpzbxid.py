# Generated by Django 5.0.3 on 2024-03-26 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0012_remove_tbhost_hostgpid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbhostgroup',
            name='gpzbxid',
            field=models.IntegerField(),
        ),
    ]
