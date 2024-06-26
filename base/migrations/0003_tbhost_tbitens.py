# Generated by Django 5.0.3 on 2024-03-24 15:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_tbhostgroup_gpusrid'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TBHost',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostzbxid', models.IntegerField()),
                ('hostname', models.CharField(max_length=50)),
                ('hostgpid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base.tbhostgroup')),
                ('hostusrid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbhost',
            },
        ),
        migrations.CreateModel(
            name='TBItens',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemzbxid', models.IntegerField()),
                ('itemname', models.CharField(max_length=50)),
                ('hostusrid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'tbitens',
            },
        ),
    ]
