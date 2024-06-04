# Generated by Django 5.0.3 on 2024-03-28 16:30

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0016_alter_tbmiddleitem_mdiitemname'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TBLayout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('layoutname', models.CharField(max_length=100)),
                ('layoutemp', models.CharField(max_length=100)),
                ('layoutlogo', models.CharField(max_length=400)),
                ('layoutdsc', models.CharField(max_length=500)),
                ('itemusrid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tblayout',
            },
        ),
        migrations.CreateModel(
            name='TBMiddleLayout',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mdiusrid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('mdlid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.tblayout')),
                ('mdlitemname', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.tbitens')),
            ],
            options={
                'db_table': 'tbmiddlelayout',
            },
        ),
    ]