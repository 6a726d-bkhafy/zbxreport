# Generated by Django 5.0.3 on 2024-03-29 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0018_rename_itemusrid_tblayout_layoutusrid_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tblayout',
            name='layoutlogo',
            field=models.FileField(blank=True, null=True, upload_to='logo'),
        ),
    ]
